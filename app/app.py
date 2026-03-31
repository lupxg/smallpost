import os
from flask import Flask
from app.config import config_by_name
from app.extensions import create_tables
from flask_restx import Api
from .routes import register_routes


def create_app():
    """
    Create a Flask application using the app factory pattern

    :return: Flask app 
    """

    app  = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv("FLASK_CONFIG", "test")])
    api = Api(
        title='smallpost',
        version='1.0',
        description='lightweith posts system',
    )

    extensions(api, app)
    register_routes(api, app, 'spost')

    return app


def extensions(api: Api, app: Flask):
    """
    Register 0 or more extensions.

    :param api: API RESTx instance
    :param app: Flask application instance
    :return: None
    """

    api.init_app(app)
    with app.app_context():
        create_tables()

    return None




app = create_app()