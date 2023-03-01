import random
import string
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import generate_password_hash, check_password_hash
from database.database import DataBaseManager

from .role import Role


db = DataBaseManager().get_db()


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_only = ('id', 'email', 'username')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __init__(self, username=None, email=None, password=None, role_id=None):
        self.username = username
        self.email = email
        self.role_id = role_id
        if password:
            self.generate_password(password)
        else:
            self.generate_password(self.__generate_random_password())

    def __repr__(self):
        return f'<User {self.username!r}>'

    def generate_password(self, password):
        self.password = generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)

    def __generate_random_password(self) -> str:
        # get random password pf length 8 with letters, digits, and symbols
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(16))
        return password

    def can(self, permission: int):
        return self.role.has_permission(permission)
