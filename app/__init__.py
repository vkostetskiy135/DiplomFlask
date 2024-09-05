from flask import Flask
from secret_key import secret_key
from app.backend.db import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Coding/DiplomFlask/app/backend/user.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = secret_key

    db.init_app(app)

    from .routers import main
    app.register_blueprint(main)

    return app
