from flask import render_template, Blueprint

post = Blueprint("post", __name__, template_folder="templates", static_folder="static")

@post.route("/")
def index():
    return render_template("post.html")