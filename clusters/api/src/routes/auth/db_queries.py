"""
This file contains a queries to the database depended on auth logic
"""
from core import database, FLUTE_DB, COL_USERS
from core.routes.auth.schemas import *


async def get_user_by_email(email: str) -> dict:
    users_table = database.get_database(FLUTE_DB).get_collection(COL_USERS)
    user        = await users_table.find_one({"email": email})
    if user:
        return {
            'name': user['name'],
            'email': user['email'],
            'login': user['login'],
            'phone': user['phone'],
            'hashed_password': user['hashed_password']
        }


async def get_user_by_login(login: str) -> dict:
    users_table = database.get_database(FLUTE_DB).get_collection(COL_USERS)
    user        = await users_table.find_one({"login": login})
    if user:
        return {
            'name': user['name'],
            'email': user['email'],
            'login': user['login'],
            'phone': user['phone'],
            'hashed_password': user['hashed_password']
        }


async def get_user_by_phone(phone: str) -> dict:
    users_table = database.get_database(FLUTE_DB).get_collection(COL_USERS)
    user        = await users_table.find_one({"phone": phone})
    if user:
        return {
            'name': user['name'],
            'email': user['email'],
            'login': user['login'],
            'phone': user['phone'],
            'hashed_password': user['hashed_password']
        }


async def get_user(determinant: str) -> dict:
    if "@" in determinant:
        return await get_user_by_email(determinant)
    if all([char.isdigit() for char in determinant]):
        return await get_user_by_phone(determinant)
    return await get_user_by_login(determinant)


async def add_user(register_form: RegisterForm, h_password: str):
    users_table = database.get_database(FLUTE_DB).get_collection(COL_USERS)
    await users_table.insert_one({
        "name"            : register_form.name,
        "email"           : register_form.email,
        "login"           : register_form.login,
        "phone"           : register_form.phone,
        "hashed_password" : h_password,
    })
