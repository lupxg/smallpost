import os
from flask import Flask
from app.extensions import db
from app.config import config_by_name

def create_app():
    app  = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv("FLASK_CONFIG", "test")])
    db.init_app(app)

    from app.posts.post import post

    app.register_blueprint(post)

    return app