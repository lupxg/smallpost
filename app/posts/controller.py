from flask_restx import Namespace, Resource, marshal, fields
from flask import request
from ..app import db
from sqlalchemy import select
from .model import Post
from http import HTTPStatus

api = Namespace('posts', description='Post related operations')

post_model = api.model("Post", {
    "id": fields.Integer,
    "title": fields.String,
    "body": fields.String,
    "created_at": fields.DateTime,
})

@api.route("/")
class PostsList(Resource):
    @api.doc('get_posts')
    @api.marshal_with(post_model, as_list=True)
    def get(self):
        """ Get a list of posts
        """

        stmt = select(Post)
        posts = db.session.execute(stmt).scalars().all()
        return posts, HTTPStatus.OK
    

    @api.response(HTTPStatus.CREATED, 'Created post')
    @api.expect(post_model)
    def post(self):
        """ Creates a new person
        """

        db.session.add(request.json)
        db.session.commit()
        return request.json, HTTPStatus.CREATED


