from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from core.routes.auth.schemas import *
from core.routes.auth import db_queries, token
from core.routes.auth.password import HashPassword
from core import STATUS, DESCRIPTION, TOKEN

router = APIRouter(
    prefix="",
    tags=["Auth"],
)


@router.post("/from_token")
async def get_current_user(jwt_token: TokenData = Depends(TokenData.as_form)):
    decoded_token = token.decode_access_token(jwt_token.token)
    if not decoded_token:
        return None
    user = await db_queries.get_user(decoded_token['user'])
    return user


@router.post("/register")
async def register(
        register_form: RegisterForm = Depends(RegisterForm.as_form)
) -> dict:

    # 1) check user credentials in database
    user_by_login = await db_queries.get_user_by_login(register_form.login)
    user_by_email = await db_queries.get_user_by_email(register_form.email)

    if user_by_email:
        return {STATUS: False, DESCRIPTION: "User with this email already exists"}
    if user_by_login:
        return {STATUS: False, DESCRIPTION: "User with this login already exists"}

    # 2) create access token
    access_token = token.create_access_token(
        data = {"user": register_form.login},
    )

    # 3) hash password
    h_password = password.HashPassword.hash(password=register_form.password)

    # 4) save user in database
    await db_queries.add_user(register_form, h_password)

    # 5) return access token
    return {"status": True, "token": Token(access_token=access_token, token_type="Bearer")}


@router.post("/login")
async def login(
        login_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> dict:
    # 1) Check user in database
    user = await db_queries.get_user(login_data.username)
    if not user:
        return {STATUS: False, DESCRIPTION: "User not found"}

    # 2) Return access token
    access_token = token.create_access_token(
        data={"user": user['login']},
    )
    return {STATUS: True, TOKEN: Token(access_token=access_token, token_type="Bearer")}