from tests.base import TestUser
from tests.base import (create_menu, create_order, create_user, create_admin, sign_in_admin,\
 sign_in_user, wrong_input_signup, empty_input_signup, empty_input_login, create_user_missing,\
 wrong_login, login_missing)


class TestUser(TestUser):
    def test_user_signup(self):
        response = self.signup_user(create_user)
        self.assertEqual(response.status_code, 201)

    def test_user_signin(self):
        self.signup_user(create_user)
        response = self.signin_user(sign_in_user)
        self.assertEqual(response.status_code, 200)

    def test_existing_user(self):
        self.signup_user(create_user)
        response = self.signup_user(create_user)
        self.assertEqual(response.status_code, 409)

    def test_wrong_signup_input(self):
        response = self.wrong_user_signup(wrong_input_signup)
        self.assertEqual(response.status_code, 400)

    def test_wrong_login_input(self):
        response = self.wrong_login_input(wrong_login)
        self.assertEqual(response.status_code, 400)

    def test_empty_signup_input(self):
        response = self.empty_signup(empty_input_signup)
        self.assertEqual(response.status_code, 400)

    def test_empty_login(self):
        response = self.empty_login(empty_input_login)
        self.assertEqual(response.status_code, 400)

    def test_missing_field_signup(self):
        response = self.missing_field_signup(create_user_missing)
        self.assertEqual(response.status_code, 400)

    def test_missing_field_login(self):
        response = self.wrong_login_input(login_missing)
        self.assertEqual(response.status_code, 400)


    