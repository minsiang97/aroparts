from models.base_model import BaseModel
from models.category import Category
import peewee as pw

class Type(BaseModel):
    name=pw.CharField(null=False)
    category=pw.ForeignKeyField(Category, backref="types", on_delete="CASCADE")