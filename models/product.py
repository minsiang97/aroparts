from models.base_model import BaseModel
from models.category import Category
import peewee as pw

class Product(BaseModel):
    name=pw.CharField(unique=True, null=False)
    description_line_1=pw.TextField(null=True)
    description_line_2=pw.TextField(null=True)
    description_line_3=pw.TextField(null=True)
    description_line_4=pw.TextField(null=True)
    description_line_5=pw.TextField(null=True)
    description_line_6=pw.TextField(null=True)
    description_line_7=pw.TextField(null=True)
    description_line_8=pw.TextField(null=True)
    description_line_9=pw.TextField(null=True)
    description_line_10=pw.TextField(null=True)
    category=pw.ForeignKeyField(Category, backref="products", on_delete = "CASCADE")
    price=pw.CharField(null=False)
    image_path=pw.CharField(null=True)
