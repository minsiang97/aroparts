import os
import config
from flask import Flask
from models.base_model import db
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.peewee import ModelView
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CSRFProtect
from models.user import User, MyAdminIndexView, AuthenticatedMenuLink
from models.product import Product
from models.category import Category
from models.image import Image

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'aroparts_web')

app = Flask('AROPARTS', root_path=web_dir)
admin = Admin(app, index_view = MyAdminIndexView())
csrf = CSRFProtect(app)

admin.add_view(ModelView(User))
admin.add_view(ModelView(Product))
admin.add_view(ModelView(Category))
admin.add_view(ModelView(Image))
admin.add_link(AuthenticatedMenuLink(name='Logout',
                                         endpoint='logout'))

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.get(User.id == user_id)

@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
