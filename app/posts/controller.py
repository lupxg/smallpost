from flask_restx import Namespace, Resource

api = Namespace('posts', description='Post related operations')


@api.route("/")
class PostsList(Resource):
    @api.doc('get_posts')
    def get(self):
        return {'message' : 'hello world from flask'}
