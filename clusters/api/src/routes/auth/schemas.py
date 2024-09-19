from pydantic import BaseModel
from fastapi  import Form


class RegisterForm(BaseModel):
    name     : str
    login    : str
    email    : str
    phone    : str
    password : str

    @classmethod
    def as_form(
            cls,
            name     : str = Form(...),
            login    : str = Form(...),
            email    : str = Form(...),
            phone    : str = Form(...),
            password : str = Form(...),
    ):
        return cls(
            name     = name,
            login    = login,
            email    = email,
            phone    = phone,
            password = password,
        )


class LoginForm(BaseModel):
    determinant : str
    password    : str

    @classmethod
    def as_form(
            cls,
            determinant : str = Form(...),
            password    : str = Form(...),
    ):
        return cls(
            determinant = determinant,
            password    = password,
        )


class User(BaseModel):
    name  : str
    email : str
    login : str
    phone : str
    hashed_password : str

    @classmethod
    def as_form(
            cls,
            name  : str = Form(...),
            email : str = Form(...),
            login : str = Form(...),
            phone : str = Form(...),
            hashed_password : str = Form(...),
    ):
        return cls(
            name  = name,
            email = email,
            login = login,
            phone = phone,
            hashed_password = hashed_password,
        )


class Token(BaseModel):
    access_token : str
    token_type   : str


class TokenData(BaseModel):
    token: str

    @classmethod
    def as_form(cls, token : str = Form(...)):
        return cls(token=token)