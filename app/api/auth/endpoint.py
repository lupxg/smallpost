from flask_restx import Namespace, Resource
from http import HTTPStatus

api = Namespace('auth', description='auth namespace')

@api.route('/resgiter')
class UserLogin(Resource):
    def post(self):
        return {'message' : 'ok'}, HTTPStatus.OK


