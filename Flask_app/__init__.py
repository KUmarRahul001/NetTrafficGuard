from flask import Flask
from flask_pymongo import PyMongo
from .utils.model_utils import random_forest_model, tuned_random_forest_model

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    mongo = PyMongo(app)

    from .routers import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Use the models as needed in your app
    # For example:
    app.config['RANDOM_FOREST_MODEL'] = random_forest_model
    app.config['TUNED_RANDOM_FOREST_MODEL'] = tuned_random_forest_model

    return app
