from sqlalchemy import Column, Integer, String
from database.database import Base
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import generate_password_hash, check_password_hash


class User(Base, SerializerMixin):
    __tablename__ = 'users'
    serialize_only = ('id', 'email', 'name')

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.generate_password(password)

    def __repr__(self):
        return f'<User {self.username!r}>'

    def generate_password(self, password):
        print('password', password)

        self.password = generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
