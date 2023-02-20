from flask import Flask
from database.database import db_session, init_db
from flask_restful import Api

from api import init_api

app = Flask(__name__)
api = Api(app)

init_db()
init_api(api)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"