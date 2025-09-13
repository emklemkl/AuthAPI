from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from .controllers.auth_controller import auth_bp
from .controllers.jwt_controller import jwt_bp
from .handlers.error_handlers import register_error_handlers

from dotenv import load_dotenv
from os import getenv

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
    app.register_blueprint(jwt_bp)
    register_error_handlers(app)
    db.init_app(app)
    app.jwt_service = JwtService(Jwt, db.session)
    app.user_service = UserService(User, db.session, app.jwt_service)
    JWTManager(app)
    return app