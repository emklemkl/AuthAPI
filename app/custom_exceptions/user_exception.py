class UserNotFoundError(Exception):
    def __init__(self, username, mail):
        self.username = username
        self.mail = mail
    
    def __str__(self):
        return f"UserNotFoundError: User '{self.username}', '{self.mail}' not found."
    
class InvalidCredentialsError(Exception):
    def __str__(self):
        return "Wrong PASSWORD or username."
    
class MissingRegistrationFieldsError(Exception):
    def __str__(self):
        return "Some fields are missing values"
    
class PasswordConfirmationMismatchError(Exception):
    def __str__(self):
        return "Password and password confirmation fields does not match"