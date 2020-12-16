from models.base_model import BaseModel
import peewee as pw
from werkzeug.security import generate_password_hash
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink
from flask_login import current_user

import re


class User(BaseModel):
    username = pw.CharField(unique=True)
    password_hash = pw.CharField(unique=False, null = False)
    is_admin = pw.BooleanField(default=1)
    password=None

    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)

        if duplicate_username and self.id != duplicate_username.id:
            self.errors.append('Username registered. Try using another username.')
        
        if self.password:
            if len(self.password)<6:
                self.errors.append("Password must be at least 6 characters.")
            
            if not re.search("[a-z]", self.password):
                self.errors.append("Password must include lowercase.")
            
            if not re.search("[A-Z]", self.password):
                self.errors.append("Password must include uppercase.")
            
            if not re.search("[\*\^\%\!\@\#\$\&]", self.password):
                self.errors.append("Password must include special characters.")
            
            if len(self.errors) == 0:
                self.password_hash = generate_password_hash(self.password)
            
        if not self.password_hash:
            self.errors.append("Password must be present")

        
    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.is_admin
        else :
            return current_user.is_authenticated

class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated