
import os


class Config(object):
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", default="minou")
    SECRET_KEY = os.environ.get("JWT_SECRET_KEY", default="super secret ultra")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQL_DATABASE", default="sqlite:///project.db")
    # set optional bootswatch theme
    FLASK_ADMIN_SWATCH = 'readable'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    TOKEN_EXPIRE_TIME = 1
    MAIL_SERVER = "localhost"
    MAIL_PORT = "1025"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", default="minou@miaou.fr")
    MAIL_PASSWORD = os.environ.get(
        "MAIL_PASSWORD", default="my secret password")


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class UnitTestConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class ProductionConfig(Config):
    ENV = "production"
