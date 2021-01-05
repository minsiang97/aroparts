from flask import Blueprint, jsonify
from models.image import Image
from models.product import Product
from models.category import Category
from models.sub_category import SubCategory

sub_categories_api_blueprint = Blueprint('sub_categories_api',
                             __name__,
                             template_folder='templates')

@sub_categories_api_blueprint.route('/<category_id>', methods=['GET'])
def index(category_id):
    category = Category.get_by_id(category_id)
    sub_categories = SubCategory.select().where(SubCategory.category == category)