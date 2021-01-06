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

@categories_api_blueprint.route('/subcategory/<id>', methods=['GET'])
def show(id):
    sub_category = SubCategory.get_by_id(id)

    return jsonify ({"id" : sub_category.id, "name" : sub_category.name, "category" : sub_category.category.name, "category_id" : sub_category.category_id})

@categories_api_blueprint.route('/<id>', methods=['GET'])
def category(id):
    category = Category.get_by_id(id)

    return jsonify({"id" : category.id, "name" : category.name})

