from models.base_model import BaseModel
from models.category import Category
import peewee as pw

class Product(BaseModel):
    name=pw.CharField(unique=True, null=False)
    description=pw.TextField(null=False)
    category=pw.ForeignKeyField(Category, backref="products", on_delete = "CASCADE")
    price=pw.CharField(null=False)
    image_path=pw.CharField(null=True)
