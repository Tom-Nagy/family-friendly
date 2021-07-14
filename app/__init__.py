from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

# Set an instance of PyMongo for communicating with the dd. 
mongo = PyMongo()

def create_app(default_config=Config):
    """
    Creates and congfigurates the app.
    Allows to use Blueprint for
    separation of concern.
    """
    app = Flask(__name__)
    # Use the Config class to set the app.
    app.config.from_object(default_config)
    # Pass the app to the PyMongo constructor
    # to ensure communication with the corresponding app.
    mongo.init_app(app)

    # Import Blueprints and register them so they can be used
    from app.users import users
    from app.home import index
    from app.create import create
    app.register_blueprint(users)
    app.register_blueprint(index)
    app.register_blueprint(create)

    return app