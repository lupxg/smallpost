import os
from flask import Flask
from app.extensions import create_tables
from flask_restx import Api
from .routes import register_routes


def create_app(config_override=None):
    """
    Create a Flask application using the app factory pattern

    :return: Flask app 
    """

    app  = Flask(__name__)
    app.config.from_object("app.config")

    if config_override:
        app.config.update(config_override)

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
