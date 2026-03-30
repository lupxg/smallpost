from flask_restx import Namespace, Resource, marshal, fields
from flask import request
from ..extensions import Session
from sqlalchemy import select
from .model import Post
from http import HTTPStatus
from pydantic import ValidationError
from app.posts.postDTO import PostDTO

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
        with Session() as session:
            posts = session.execute(stmt).scalars().all()
        return posts, HTTPStatus.OK
    

    @api.response(HTTPStatus.CREATED, 'Created post')
    @api.expect(post_model)
    def post(self):
        """ Creates a new person
        """

        with Session() as session:
            user_post = request.get_json()
            postDTO = PostDTO(**user_post)
            post = Post(**vars(postDTO))
        
            session.add(post)
            session.commit()
        return request.json, HTTPStatus.CREATED


