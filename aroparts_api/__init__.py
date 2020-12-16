from app import app, csrf
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from aroparts_api.blueprints.products.views import products_api_blueprint
from aroparts_api.blueprints.images.views import images_api_blueprint

csrf.exempt(products_api_blueprint)
csrf.exempt(images_api_blueprint)

app.register_blueprint(products_api_blueprint, url_prefix='/api/v1/products')
app.register_blueprint(images_api_blueprint, url_prefix='/api/v1/images')
