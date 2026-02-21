import os
from flask import Flask
from app.extensions import db
from app.config import config_by_name
from flask_restx import Api

def create_app():
    app  = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv("FLASK_CONFIG", "test")])
    db.init_app(app)
    api = Api(
        title='smallpost',
        version='1.0',
        description='lightweith posts system',
        # All API metadatas
    )
    
    from app.posts.post import post

    app.register_blueprint(post)

    return app