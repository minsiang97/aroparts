from models.base_model import BaseModel
from models.category import Category
import peewee as pw

class SubCategory(BaseModel):
    name=pw.CharField(null=False)
    category = pw.ForeignKeyField(Category, backref="sub_categories", on_delete="CASCADE", null=True)
    