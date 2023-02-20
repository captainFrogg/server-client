from flask import Flask
from flask_restful import Api, Resource
from database.models.user import User
from database.database import db_session

app = Flask(__name__)
api = Api(app)

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        return user.to_dict()
