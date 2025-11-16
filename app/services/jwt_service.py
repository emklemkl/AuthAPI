from sqlalchemy import or_, select

from flask_jwt_extended import create_access_token

class JwtService():
    user = None
    def __init__(self, jwt_model, db_session):
        self.db_session = db_session
        self.jwt_model = jwt_model

    def jwt_exists(self, id) :
        pass
        # select(User, Jwt).join(User.id)

    @staticmethod
    def generate_access_token(user_credentials):
        access_token = create_access_token(user_credentials.username)
        return access_token

    def save_access_token(self, user, access_token):
        pass
        # jwt = self.Jwt(user.user_id=2, token=access_token)
        # self.db_session.add(jwt)
        # self.db_session.commit()

    def get_token_user(self, user_credentials):
        self.db_session.execute(select(self.User)).scalars().all()

    def get_all_user_token(self, user, user_id): #TODO Fix getting att tokens for a user
        u=self.db_session.get(user, user_id)
        for token in u.tokens:
            print(token.token, token.expires_at)

        return self.db_session.get(user, user_id)

