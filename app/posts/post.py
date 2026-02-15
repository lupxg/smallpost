from flask import Blueprint, jsonify, abort
from http import HTTPStatus
from ..extensions import db
from sqlalchemy import text

post = Blueprint("post", __name__)

@post.route("/", methods=["GET"])
def index():
    return jsonify({"message" : "hello world from Flask"}), HTTPStatus.OK

@post.route("/health")
def health():
    try:
        db.session.execute(text("SELECT 1"))
        return {"status": "ok"}, HTTPStatus.OK  
    except Exception as e:
        return jsonify(error=str(e)), HTTPStatus.BAD_REQUEST