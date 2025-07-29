from fastapi import HTTPException, status

class UserAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code= 400,
            detail="User already exists."
        )
class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code= 401,
            detail="Invalid username or password"
        )

class IncorrectOldPasswordException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code= 400,
            detail="Old password is incorrect."
        )

class SamePasswordException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="New password must be different from previously used passwords."
        )
class PasswordExpiredException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="Please change your password."
        )

class MaxAttemptsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=429,
            detail="Max attempts reached."
        )

class AccountDeactivatedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="Account temporarily deactivated."
        )