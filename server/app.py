from flask import Flask
from database.database import db_session, init_db

app = Flask(__name__)
init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"