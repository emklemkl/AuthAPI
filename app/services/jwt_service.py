from dataclasses import asdict
from flask import request, jsonify, current_app, abort 
from sqlalchemy import or_, select
from app.custom_exceptions.user_exception import UserNotFoundError, InvalidCredentialsError, MissingRegistrationFieldsError, PasswordConfirmationMismatchError
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


class JwtService():
    def __init__(self, Jwt, db_session):
        self.db_session = db_session
        self.Jwt = Jwt
    
    def jwt_exists(self, id) :
        pass
        # select(User, Jwt).join(User.id)

    def _create_access_token(self, user_credentials):
        access_token = create_access_token("Wilson87-TEST") # TODO
        jwt = self.Jwt(user_id=2, token=access_token)
        self.db_session.add(jwt)
        self.db_session.commit() 
        return access_token

    def get_token_user(self, user_credentials):
        self.db_session.execute(select(self.User)).scalars().all()

    def get_all_user_token(self, user, user_id): #TODO Fix getting att tokens for a user
        u=self.db_session.get(user, user_id)
        for token in u.tokens:
            print(token.token, token.expires_at)

        return self.db_session.get(user, user_id)

