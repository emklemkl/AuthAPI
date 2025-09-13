from flask import Blueprint, request, jsonify, current_app

jwt_bp = Blueprint("jwt", __name__, url_prefix="/jwt")
