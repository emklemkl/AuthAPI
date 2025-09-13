from flask import Blueprint, request, jsonify, current_app

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = current_app.user_service.register_user(data)
    return jsonify({"msg": f"User '{user.username}' was registered."}), 205

@auth_bp.route("/login", methods=["POST"])
def login():
        req = request.json
        user = current_app.user_service.get_user(req)

        token = current_app.user_service.login_user(user, req.get("password"))
        return jsonify(
                {
                "access_token": token,
                "token_type":"Bearer",
                "expires_in":3600,
                "user": {
                        "id": user.id,
                        "username": user.username
                }}), 200

                # TODO "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA"
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

# @auth_bp.route("/jwt_token", methods=["POST"])
# def jwt_token():
#         token = current_app.user_service.login_user(request.json)
#         return jsonify({"msg": f"User: {token.username} logged in."}), 205

@auth_bp.route("/jwt_token", methods=["POST"])
def get_jwt_token():
        print("-----")
        print("-----")
        print(request.json.get("id"))
        print("-----")
        print("-----")
        token = current_app.user_service.get_all_user_token(request.json.get("id"))
        return jsonify({"msg": f"User: logged in."}), 205

