from flask import Blueprint, jsonify
from models.image import Image
from models.product import Product
from models.type import Type
from models.category import Category

images_api_blueprint = Blueprint('images_api',
                             __name__,
                             template_folder='templates')

@images_api_blueprint.route('/<product_id>', methods=['GET'])
def index(product_id):
    product = Product.get_by_id(product_id)   
    images = Image.select().where(Image.product == product)
    return jsonify ([{"id" : i.id, "product" : i.product.name, "category" : i.category_id, "type" : i.type_id, "url" : i.new_image_url, "description" : i.product.description} for i in images])

