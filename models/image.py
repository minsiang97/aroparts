from models.base_model import BaseModel
from models.category import Category
from models.product import Product
from models.type import Type
from playhouse.hybrid import hybrid_property
import peewee as pw

class Image(BaseModel):
    product=pw.ForeignKeyField(Product, backref="images", on_delete="CASCADE")
    category=pw.ForeignKeyField(Category, backref="images", on_delete="CASCADE")
    type=pw.ForeignKeyField(Type, backref="images", on_delete="CASCADE")
    image_path=pw.CharField(default='https://aroparts.s3-ap-southeast1.amazonaws.com/logo.png')

    @hybrid_property
    def new_image_url(self):
        return self.image_path