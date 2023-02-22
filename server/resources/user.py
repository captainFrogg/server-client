from flask import Flask
from flask_jwt_extended import jwt_required
from flask_restful import Api, Resource
from database.models.user import User
from database.database import db_session

app = Flask(__name__)
api = Api(app)


class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.get(user_id)
        return user.to_dict() if user else "No User Found"
