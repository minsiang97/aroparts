from flask import Blueprint, jsonify
from models.image import Image
from models.product import Product
from models.type import Type
from models.category import Category

products_api_blueprint = Blueprint('products_api',
                             __name__,
                             template_folder='templates')

@products_api_blueprint.route('type/<type_id>', methods=['GET'])
def index(type_id):
    type = Type.get_by_id(type_id)
    products = Product.select().where(Product.type == type)
    return jsonify ([{"id" : p.id, "product_name" : p.name, "category" : p.category_id, "type" : p.type_id, "description" : p.description, "price" : p.price, "url" : p.image_path} for p in products])

@products_api_blueprint.route('/<product_id>', methods=['GET'])
def product(product_id):
    product = Product.get_by_id(product_id)
    return jsonify({"id" : product.id, "product_name" : product.name, "category" : product.category_id, "type" : product.type_id, "description" : product.description, "price" : product.price, "url" : product.image_path})

