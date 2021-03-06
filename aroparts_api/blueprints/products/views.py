from flask import Blueprint, jsonify
from models.image import Image
from models.product import Product
from models.category import Category
from models.sub_category import SubCategory
from models.product_category import ProductCategory

products_api_blueprint = Blueprint('products_api',
                             __name__,
                             template_folder='templates')

@products_api_blueprint.route('category/<category_id>', methods=['GET'])
def index(category_id):
    category = Category.get_by_id(category_id)
    products = ProductCategory.select().where(ProductCategory.category == category)

    return jsonify ([{"id" : p.product_id, "product_name" : p.product.name, "product_chinese_name" : p.product.chinese_name, "category" : p.product.category_id, "price" : p.product.price, "url" : p.product.image_path} for p in products])

@products_api_blueprint.route('/<product_id>', methods=['GET'])
def product(product_id):
    product = Product.get_by_id(product_id)
    return jsonify({"id" : product.id, "product_name" : product.name, "product_chinese_name" : product.chinese_name, "category" : product.category.name, "category_id" : product.category_id, "sub_category_id" : product.sub_category_id, "sub_category" : product.sub_category.name,  "description_line_1" : product.description_line_1, "description_line_2" : product.description_line_2, "description_line_3" : product.description_line_3, "description_line_4" : product.description_line_4, "description_line_5" : product.description_line_5, "description_line_6" : product.description_line_6, "description_line_7" : product.description_line_7, "description_line_8" : product.description_line_8, "description_line_9" : product.description_line_9, "description_line_10" : product.description_line_10, "price" : product.price, "url" : product.image_path})

@products_api_blueprint.route('/', methods=['GET'])
def products():
    products = Product.select()
    return jsonify ([{"id" : p.id, "product_name" : p.name, "product_chinese_name" : p.chinese_name, "category" : p.category_id, "price" : p.price, "url" : p.image_path} for p in products])

@products_api_blueprint.route('/category/sub_category/<sub_category_id>', methods=['GET'])
def sub_category_products(sub_category_id):
    sub = SubCategory.get_or_none(SubCategory.id == sub_category_id)
    products = ProductCategory.select().where(ProductCategory.sub_category == sub)
    if products :
        return jsonify ([{"id" : p.product_id, "product_name" : p.product.name, "product_chinese_name" : p.product.chinese_name, "category" : p.category.name, "price" : p.product.price, "url" : p.product.image_path, "sub_category" : p.sub_category.name} for p in products])
    else :
        return jsonify ({"message" : "No products found"})
