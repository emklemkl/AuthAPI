from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, select
from app.utils.validators import passwords_match
from app.custom_exceptions.user_exception import UserNotFoundError, InvalidCredentialsError, MissingRegistrationFieldsError, PasswordConfirmationMismatchError

class UserService():
    def __init__(self, user_model, db_session, jwt_service):
        self.User = user_model
        self.db_session = db_session
        self.jwt_service = jwt_service


    def get_user(self, user_credentials_json):
        stmt = select(self.User).where(self.User.username == user_credentials_json.get("username"))
        result = self.db_session.execute(stmt)
        user = result.scalar_one_or_none()
        if user is None:
            raise InvalidCredentialsError()
        return user

    def get_all_users(self):
        users = self.db_session.execute(select(self.User)).scalars().all()
        if not users:
            raise UserNotFoundError("ALL EXISTING", "USERS") #TODO Maybe replace this with InvalidCredentialsError in prod
        return users

    def register_user(self, credentials_json):
        username = credentials_json.get("username")
        email = credentials_json.get("email")
        password = credentials_json.get("password")
        password_confirm = credentials_json.get("password_confirm")
        
        if not all([username, email, password, password_confirm]):
            raise MissingRegistrationFieldsError

        if not passwords_match(password, password_confirm):
            raise PasswordConfirmationMismatchError

        try:
            with self.db_session.begin():  # Starts a transaction block
                user = self.User(username=username, email=email)
                user.set_password_hash(password)
                self.db_session.add(user)
                self.db_session.commit() 
            return user
        except SQLAlchemyError as e:
            self.db_session.rollback()  # Optional, since .begin() handles rollback
            raise e  #TODO Or raise a custom error if you prefer 

    def delete_user(self, id): #TODO
        pass

    def get_all_user_token(self, id):
        return self.jwt_service.get_all_user_token(self.User, id)
        