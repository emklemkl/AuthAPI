from flask import Flask

from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select

from .controllers.auth_controller import auth_bp
from .custom_exceptions.user_exception import UserNotFoundError

from .handlers.error_handlers import register_error_handlers

from dotenv import load_dotenv
from os import getenv

from .services import jwt_service


class Base(DeclarativeBase):
    pass

load_dotenv()

db = SQLAlchemy(model_class=Base)

def create_app():
    app = Flask(__name__)

    from .models.user import User
    from .models.jwt import Jwt
    from .services.user_service import UserService
    from .services.jwt_service import JwtService
    app.config["JWT_SECRET_KEY"] = getenv("JWT_SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
    app.register_blueprint(auth_bp)
    register_error_handlers(app)
    db.init_app(app)
    app.jwt_service = JwtService(Jwt, db.session)
    app.user_service = UserService(User, db.session, app.jwt_service)
    jwt = JWTManager(app)
    @jwt.user_lookup_loader
    def user_lookup(_jwt_header, jwt_data):
        user = db.session.execute(select(User).where(User.username == jwt_data["sub"])).scalar_one_or_none()
        if user.username == jwt_data["sub"]:
            return user
        raise UserNotFoundError(jwt_data["sub"])
    return app
