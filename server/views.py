import json

from flask import jsonify, request
from flask_jwt_extended import create_access_token
from database.models.user import User
from app import db_session


def init_routes(app):
    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/login", methods=['POST'])
    def login():
        username = request.json.get("name", None)
        password = request.json.get("password", None)

        user = User.query.filter_by(name=username).first()

        if user is None:
            return jsonify({"msg": "Bad username or password"}), 401

        if user.check_password(password):
            access_token = create_access_token(identity=username)

            return jsonify(access_token=access_token)

        return jsonify({"msg": "Bad username or password"}), 401

    @app.route("/sign-up", methods=['POST'])
    def sign_up():
        print('request', request.data)
        params = json.loads(request.data)
        print('params', params)

        name = params['name']
        email = params['email']
        password = params['password']
        user = User(name, email, password)
        db_session.add(user)
        db_session.commit()
        return "user creation success"
