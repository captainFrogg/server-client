from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.database import DataBaseManager

from api import init_api

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_SECRET_KEY"] = "minou"  # Change this!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db_manager = DataBaseManager()
db_manager.initialize_db(app)
init_api(api)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db = db_manager.get_db()
    db.session.remove()


@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:4200"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] =\
        "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] =\
        ("Accept, Content-Type, Content-Length, Accept-Encoding" +
            "X-CSRF-Token, Authorization")
    return response
