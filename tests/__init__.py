from config import TestConfig
from app import app

create_admin = {
    "name": "ronald",
    "username": "ron",
    "email": "okello@mail.com",
    "password": "king"
}
create_user = {
    "name": "kica",
    "username": "ronn12",
    "email": "okelloer@mail.com",
    "password": "12345"
}

create_menu = {"name": "matooke", "price": "15000"}

create_order = {"amount": "5", "food": "1"}

sign_in_admin = {"username": "ron", "password": "king"}
sign_in_user = {"username": "ronn12", "password": "12345"}
wrong_input_signup = {
    "name": "kica",
    "username": "ronn12",
    "email": "okellmail.com",
    "password": "12345"
}
empty_input_signup = {
    "name": "kica",
    "username": "",
    "email": "okello@mail.com",
    "password": ""
}

empty_input_login = {"username": "", "password": "12345"}
create_user_missing = {
    "username": "ronn12",
    "email": "okello@mail.com",
    "password": "12345"
}
login_missing = {"password": "12345"}
wrong_login = {"username": "@//", "password": "12345"}

missing_order_field = {"food": "2"}
empty_space_order = {"amount": "", "food": ""}
wrong_order_input = {"amount": "ksd", "food": "lk"}

missing_menu = {"price": "15000"}
empty_menu = {"name": "", "price": ""}
new_menu = {"name": "chicken", "price": "4000"}
update_order = {"status": "Complete"}
