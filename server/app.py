from flask import Flask
from database.database import db_session, init_db
from flask_restful import Api
from flask_bcrypt import Bcrypt

from api import init_api
from login import login_manager
from views import init_routes

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
init_db()
init_api(api)
login_manager.init_app(app)
init_routes(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
