from tests.base import TestUser
from tests.base import missing_order_field, empty_space_order, wrong_order_input, create_admin,\
create_menu, create_order, missing_menu, empty_menu, new_menu

class TestApp(TestUser):
    def test_missing_order_field(self):
        response = self.missing_order_field(missing_order_field)
        self.assertEqual(response.status_code, 400)

    def test_empty_space_order(self):
        response = self.empty_space_order(empty_space_order)
        self.assertEqual(response.status_code, 400)

    def test_wrong_order_input(self):
        response = self.wrong_order_input(wrong_order_input)
        self.assertEqual(response.status_code, 400)

    # def test_add_order(self):
    #     self.create_menu(create_menu)
    #     response = self.add_order(create_order)
    #     self.assertEqual(response.status_code, 201)

    def test_create_menu(self):
        response = self.create_menu(new_menu)
        self.assertEqual(response.status_code, 201)

    def test_missing_menu(self):
        response = self.missing_menu(missing_menu)
        self.assertEqual(response.status_code, 400)

    def test_empty_menu(self):
        response = self.empty_menu(empty_menu)
        self.assertEqual(response.status_code, 400)

    def test_get_menu(self):
        response = self.get_menu()
        self.assertEqual(response.status_code, 200)

    def duplicate_menu(self):
        response = self.create_menu(new_menu)   
        self.assertEqual(response.status_code, 409) 