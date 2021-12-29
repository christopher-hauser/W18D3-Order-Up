import os


class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "postgresql://order_up:9uCxydbt@localhost/order_up_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
