import json

from flask import request
from database.models.user import User
from app import db_session


def init_routes(app):
    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/login", methods=['POST'])
    def login():
        params = json.loads(request.data)
        username = params.name
        password = params.password
        # user = User.query.

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
