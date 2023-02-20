from sqlalchemy import Column, Integer, String
from database.database import Base
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin


class User(Base, SerializerMixin, UserMixin):
    __tablename__ = 'users'
    serialize_only = ('email', 'name')

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'
