from flask import Flask
from small_post.extensions import db

def create_app():
    app  = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)

    from small_post.posts.post import post

    app.register_blueprint(post)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")