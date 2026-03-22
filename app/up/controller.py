from flask_restx import Namespace, Resource
from sqlalchemy import text
from app.extensions import db

api = Namespace('up', description='Post related operations')

@api.route("/")
class Health(Resource):
    @api.doc('check app healthy')
    def get(self):
        return {'message' : 'ok'}
    

@api.route("/database")
class HealthDatabase(Resource):
    @api.doc('check database healthy')
    def get(self):
        with db.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return ""
    
