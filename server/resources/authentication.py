from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from database.database import DataBaseManager


from database.models.user import User

db: SQLAlchemy = DataBaseManager().get_db()


class LoginResource(Resource):
    def post(self):
        body = request.get_json()
        user: User = User.query.filter_by(username=body['username']).first()

        if user is None:
            return make_response(jsonify({"msg": "Bad username or password"}), 400)

        if user.check_password(body['password']):
            access_token = create_access_token(identity=body['username'])

            return make_response(jsonify({"access_token": access_token}), 200)

        return make_response(jsonify({"msg": "Bad username or password"}), 400)


class SignUpResource(Resource):
    def post(self):
        body = request.get_json()
        username = body['username']
        email = body['email']
        password = body['password']
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()
        return make_response(jsonify({"msg": "user creation success"}), 200)
