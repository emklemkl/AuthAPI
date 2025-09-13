from flask import jsonify

from app.custom_exceptions.user_exception import UserNotFoundError, InvalidCredentialsError, MissingRegistrationFieldsError, PasswordConfirmationMismatchError

def handle_user_not_found(error):
    return jsonify({"msg": str(error)}), 404
    
def handle_invalid_credentials(error):
    return jsonify({"msg": str(error)}), 401

def handle_missing_registration_field_error(error):
    return jsonify({"msg": str(error)}), 400

def handle_password_confirmation_mismatch_error(error):
    return jsonify({"msg": str(error)}), 400


def register_error_handlers(app):
    app.register_error_handler(UserNotFoundError, handle_user_not_found)
    app.register_error_handler(InvalidCredentialsError, handle_invalid_credentials)
    app.register_error_handler(MissingRegistrationFieldsError, handle_missing_registration_field_error)
    app.register_error_handler(PasswordConfirmationMismatchError, handle_password_confirmation_mismatch_error)
