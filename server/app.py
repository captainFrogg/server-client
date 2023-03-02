from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.database import DataBaseManager
from flask_admin import Admin


from api import init_api
from admin import init_admin_view, MyAdminIndexView
from routes import init_routes

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_SECRET_KEY"] = "minou"  # TODO: Change this!
app.secret_key = "super secret ultra"  # TODO: Change this!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# set optional bootswatch theme
# app.config['FLASK_ADMIN_SWATCH'] = 'readable'
api = Api(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)
jwt = JWTManager(app)
admin = Admin(app,  base_template='admin.html',  template_mode='bootstrap4', index_view=MyAdminIndexView(
    name='Home',
))
db_manager = DataBaseManager()
db_manager.initialize_db(app)
init_admin_view(admin, db_manager.get_db())
init_routes(app=app)
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


@login.user_loader
def load_user(id):
    from database.models.user import User
    return User.query.get(int(id))
