from flask import Flask, jsonify
# from mysql.connector import connect, Error

def create_app():
    app  = Flask(__name__)

    # Registering blueprints.
    from small_post.posts.post import post

    app.register_blueprint(post)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")