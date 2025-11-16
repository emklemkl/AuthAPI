from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.jwt_service import JwtService


from app.custom_exceptions.user_exception import InvalidCredentialsError

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = current_app.user_service.register_user(data)
    return jsonify({"msg": f"User '{user.username}' was registered."}), 205

@auth_bp.route("/login", methods=["POST"])
def login():
        try:
            req = request.json

            if not req or "password" not in req or not req["password"]: # TODO Pydantic for validation https://docs.pydantic.dev/latest/#why-use-pydantic https://pypi.org/project/flask-pydantic-api/
                return jsonify({"msg": "Password is required"}), 400

            user = current_app.user_service.get_user(req)
            user.check_password(req.get("password"))
            token = JwtService.generate_access_token(user)
            return jsonify(
                    {
                    "access_token": token,
                    "token_type":"Bearer",
                    "expires_in":3600,
                    "user": {
                            "id": user.id,
                            "username": user.username
                    }}), 200
        except InvalidCredentialsError as e:
            return jsonify({"msg": f"{e}"}), 401


@auth_bp.route("/validate_token", methods=["POST"])
@jwt_required()
def jwt_token():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200


@auth_bp.route("/get_all_users", methods=["GET"])
def get_all_users():
        users = current_app.user_service.get_all_users()
        print(type(users))
        for u in users:
                print(u.username)
        return jsonify({"msg": f"{users}get_all_users is #TODO."}), 205

@auth_bp.route("/delete", methods=["POST"])
def delete():
        token = current_app.user_service.login_user(request.json)
        return jsonify({"msg": f"User: {token.username} logged in."}), 205
