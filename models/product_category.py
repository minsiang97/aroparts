from models.base_model import BaseModel
import peewee as pw
from models.category import Category
from models.product import Product
from models.sub_category import SubCategory

class ProductCategory(BaseModel):
    product=pw.ForeignKeyField(Product, backref="categories", on_delete = "CASCADE")
    category=pw.ForeignKeyField(Category, backref="products", on_delete = "CASCADE")
    sub_category=pw.ForeignKeyField(SubCategory, backref="products", on_delete="CASCADE", null=True)