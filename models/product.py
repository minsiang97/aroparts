from models.base_model import BaseModel
from models.category import Category
from models.sub_category import SubCategory
import peewee as pw

class Product(BaseModel):
    name=pw.CharField(unique=False, null=False)
    chinese_name = pw.CharField(unique=False, null=True)
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
    sub_category=pw.ForeignKeyField(SubCategory, backref="products", on_delete = "CASCADE", null=True)
    price=pw.CharField(null=False)
    image_path=pw.CharField(null=True)
