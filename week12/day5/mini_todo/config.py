import os

appAbsolutePath = os.path.dirname(__file__)


class Config:
    SECRET_KEY = "secret-very-secret"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{appAbsolutePath}/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


