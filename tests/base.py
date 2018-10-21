import unittest
import os
from app import app
from tests import (create_menu, create_order, create_user, create_admin, sign_in_admin, sign_in_user\
,wrong_input_signup, empty_input_login, empty_input_signup, create_user_missing, wrong_login, login_missing,\
missing_order_field, empty_space_order, wrong_order_input, missing_menu, empty_menu, new_menu, update_order)
from app import views
from app.dboperations import Menu, Order
import json
from config import TestConfig
from app.models import Database

app.config.from_object(TestConfig)

db = Database()


class TestUser(unittest.TestCase):
    def setUp(self):

        self.client = app.test_client()
        db.create_menu_table()
        db.create_user_table()
        db.create_orders_table()

    def tearDown(self):
        clear_users = "DROP TABLE users CASCADE"
        db.cur.execute(clear_users)
        clear_menu = "DROP TABLE menu CASCADE"
        db.cur.execute(clear_menu)
        clear_orders = "DROP TABLE orders CASCADE"
        db.cur.execute(clear_orders)

    def signup_admin(self, create_admin):
        response = self.client.post("/api/v1/auth/admin",\
        data = json.dumps(create_admin), content_type = 'application/json')
        response_data = json.loads(response.data.decode())
        return response_data["access_token"]

    def signup_user(self, create_user):
        response = self.client.post("/api/v1/auth/signup",\
        data = json.dumps(create_user), content_type = 'application/json')
        return response

    def signin_user(self, sign_in_user):
        response = self.client.post("api/v1/auth/login",\
        data = json.dumps(sign_in_user), content_type = 'application/json')
        return response

    def user_token(self, sign_in_user):
        response = self.client.post("api/v1/auth/login",\
        data = json.dumps(sign_in_user), content_type = 'application/json')
        response_data = json.loads(response.data.decode())
        return response_data["access_token"]

    def wrong_user_signup(self, wrong_input_signup):
        response = self.client.post("/api/v1/auth/signup",\
        data = json.dumps(wrong_input_signup), content_type = 'application/json')
        return response

    def empty_signup(self, empty_input_signup):
        response = self.client.post("/api/v1/auth/signup",\
        data = json.dumps(empty_input_signup), content_type = 'application/json')
        return response

    def missing_field_signup(self, create_user_missing):
        response = self.client.post("/api/v1/auth/signup",\
        data = json.dumps(create_user_missing), content_type = 'application/json')
        return response

    def empty_login(self, empty_input_login):
        response = self.client.post("/api/v1/auth/login",\
        data = json.dumps(empty_input_login), content_type = 'application/json')
        return response

    def missing_field_login(self, login_missing):
        response = self.client.post("/api/v1/auth/login",\
        data = json.dumps(login_missing), content_type = 'application/json')
        return response

    def wrong_login_input(self, wrong_login):
        response = self.client.post("/api/v1/auth/login",\
        data = json.dumps(wrong_login), content_type = 'application/json')
        return response

    def missing_order_field(self, missing_order_field):
        response = self.client.post("/api/v1/users/orders",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,data = json.dumps(missing_order_field), content_type = 'application/json')
        return response

    def empty_space_order(self, empty_space_order):
        response = self.client.post("/api/v1/users/orders",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,data = json.dumps(missing_order_field), content_type = 'application/json')
        return response

    def wrong_order_input(self, wrong_order_input):
        response = self.client.post("/api/v1/users/orders",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,data = json.dumps(wrong_order_input), content_type = 'application/json')
        return response

    def add_order(self, create_order):
        response = self.client.post("/api/v1/users/orders",headers={'Authorization':\
         'Bearer '+ self.user_token(sign_in_user)}\
        ,data = json.dumps(create_order), content_type = 'application/json')
        return response

    def create_menu(self, create_menu):
        response = self.client.post("/api/v1/menu",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,data = json.dumps(create_menu), content_type = 'application/json')
        return response

    def missing_menu(self, missing_menu):
        response = self.client.post("/api/v1/menu",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,data = json.dumps(missing_menu), content_type = 'application/json')
        return response

    def empty_menu(self, empty_menu):
        response = self.client.post("/api/v1/menu",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,data = json.dumps(empty_menu), content_type = 'application/json')
        return response

    def get_menu(self):
        response = self.client.get(
            "/api/v1/menu", content_type='application/json')
        return response

    def get_all_orders(self):
        response = self.client.get("/api/v1/orders",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,content_type = 'application/json')
        return response

    def get_all_orders_no_authorization(self):
        response = self.client.get("/api/v1/orders",headers={'Authorization':\
         'Bearer '+ self.user_token(sign_in_user)}\
        ,content_type = 'application/json')
        return response

    def get_one_order(self):
        response = self.client.get("/api/v1/orders/1",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,content_type = 'application/json')
        return response

    def get_one_order_not_authorised(self):
        response = self.client.get("/api/v1/orders",headers={'Authorization':\
         'Bearer '+ self.user_token(sign_in_user)}\
        ,content_type = 'application/json')
        return response

    def get_one_order_wrong_input(self):
        response = self.client.get("/api/v1/orders/a",headers={'Authorization':\
         'Bearer '+ self.signup_admin(create_admin)}\
        ,content_type = 'application/json')
        return response

    def update_order(self, update_order):
        response = self.client.put("/api/v1/orders/1",headers={'Authorization':\
         'Bearer '+ self.user_token(sign_in_admin)}\
        ,data=json.dumps(update_order), content_type = 'application/json')
        return response

    def update_order_not_admin(self, update_order):
        response = self.client.put("/api/v1/orders/1",headers={'Authorization':\
         'Bearer '+ self.user_token(sign_in_user)}\
        ,data=json.dumps(update_order), content_type = 'application/json')
        return response
