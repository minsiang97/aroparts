from models.base_model import BaseModel
from models.category import Category
from models.type import Type
import peewee as pw

class Product(BaseModel):
    name=pw.CharField(unique=True, null=False)
    description=pw.TextField(null=False)
    category=pw.ForeignKeyField(Category, backref="products", on_delete = "CASCADE")
    type=pw.ForeignKeyField(Type, backref="products", on_delete = "CASCADE", null=True)
    price=pw.DecimalField(decimal_places = 2)
