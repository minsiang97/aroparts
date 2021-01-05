from flask import Blueprint, jsonify
from models.image import Image
from models.product import Product
from models.category import Category
from models.sub_category import SubCategory

categories_api_blueprint = Blueprint('categories_api',
                             __name__,
                             template_folder='templates')

@categories_api_blueprint.route('/', methods=['GET'])
def index():
    categories = Category.select()

    return jsonify ([{"id" : c.id, "name" : c.name, "sub_categories" : [{"sub" : s.name, "id" : s.id}for s in c.sub_categories]} for c in categories])
