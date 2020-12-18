from flask import Blueprint, jsonify
from models.image import Image
from models.product import Product
from models.category import Category

products_api_blueprint = Blueprint('products_api',
                             __name__,
                             template_folder='templates')

@products_api_blueprint.route('category/<category_id>', methods=['GET'])
def index(category_id):
    category = Category.get_by_id(category_id)
    products = Product.select().where(Product.category == category)
    return jsonify ([{"id" : p.id, "product_name" : p.name, "category" : p.category_id, "description" : p.description, "price" : p.price, "url" : p.image_path} for p in products])

@products_api_blueprint.route('/<product_id>', methods=['GET'])
def product(product_id):
    product = Product.get_by_id(product_id)
    return jsonify({"id" : product.id, "product_name" : product.name, "category" : product.category_id,  "description" : product.description, "price" : product.price, "url" : product.image_path})

