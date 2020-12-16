from flask import Blueprint, jsonify
from models.image import Image
from models.product import Product
from models.type import Type
from models.category import Category

images_api_blueprint = Blueprint('images_api',
                             __name__,
                             template_folder='templates')

@images_api_blueprint.route('/<category_id>/<type_id>/', methods=['GET'])
def index(category_id, type_id):
    category = Category.get_by_id(category_id)
    type = Type.get_by_id(type_id)
    products = Product.select().where(Product.category == category, Product.type == type)
    images = Image.select().where(Image.product.in_(products))
    return jsonify ([{"id" : i.id, "product" : i.product.name, "category" : i.category_id, "type" : i.type_id, "url" : i.image_path, "description" : i.product.description} for i in images])

