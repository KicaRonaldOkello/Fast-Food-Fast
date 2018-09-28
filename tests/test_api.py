import unittest
from app import app
from app import views
from app.models import Menu, Order
import json

class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_order(self):
        order = {
            "name": "ronald",
            "amount": "2",
            "food": "1"
        }
        post_order = Order()
        response = self.client.post("/api/v1/orders", data = json.dumps(order), content_type = 'application/json')
        self.assertEqual(post_order.ORDER[0]["name"], "ronald")
        self.assertEqual(post_order.ORDER[0]["amount"], "2")
        self.assertEqual(post_order.ORDER[0]["food"], 1)
        self.assertEqual(response.status_code, 201)

    def test_add_menu(self):
        menu = {
            "name": "chicken",
            "price": 2000
        }
        response = self.client.post("/api/v1/menu", data = json.dumps(menu), content_type = 'application/json')
        menu = Menu()
        self.assertEqual(len(menu.MENU), 1)
        self.assertEqual(menu.MENU[0]["name"], "chicken")
        self.assertEqual(menu.MENU[0]["price"], 2000)
        self.assertEqual(response.status_code, 201)

    def test_get_menu(self):
        menu = Menu()
        menu_item = menu.get_menu()
        self.assertEqual(menu_item[0]["food_id"], 1)
        self.assertEqual(menu_item[0]["name"], "chicken")
        self.assertEqual(menu_item[0]["price"], 2000)
        response = self.client.get("/api/v1/menu")
        self.assertEqual(response.status_code, 200)

    def test_get_order(self):
        order = {
            "name": "ron",
            "amount": "3",
            "food": "1"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), content_type = 'application/json')
        order = Order()
        get_order = order.get_orders()
        self.assertEqual(get_order[0]["order_no"], 1)
        self.assertEqual(get_order[1]["order_no"], 2)
        response = self.client.get("/api/v1/orders")
        self.assertEqual(response.status_code, 200)

    def test_get_an_order(self):
        order = Order()
        get_one_order = order.get_an_order(1)
        self.assertEqual(get_one_order[0]["order_no"], 1)
        self.assertEqual(get_one_order[0]["food"], "chicken")
        self.assertEqual(get_one_order[0]["name"], "ronald")
        response = self.client.get("/api/v1/orders/1")
        self.assertEqual(response.status_code, 200)

    def test_update_order(self):
        status = {
            "status": "Accepted"
        }
       
        order = Order()
        old_order = order.get_an_order(1)
        self.assertEqual(old_order[0]["order_status"], "Pending")
        response = self.client.put("/api/v1/orders/1", data = json.dumps(status), content_type = 'application/json')
        new_order = order.get_an_order(1)
        self.assertEqual(new_order[0]["order_status"], "Accepted")
        self.assertEqual(response.status_code, 201)

    def test_if_empty_order_posted(self):
        order = {
            "name": "",
            "amount": "",
            "food": ""
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_if_empty_menu_posted(self):
        menu = {
            "name": "",
            "price": ""
        }
        response = self.client.post("/api/v1/menu", data = json.dumps(menu), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_duplication_in_menu(self):
        menu = {
            "name": "chicken",
            "price": 2000
        }
        response = self.client.post("/api/v1/menu", data = json.dumps(menu), content_type = 'application/json')
        self.assertEqual(response.status_code, 409)

    def test_aan_empty_menu(self):
        response = self.client.get("/api/v1/menu")
        self.assertEqual(response.status_code, 204)

    def test_aan_empty_order(self):
        response = self.client.get("/api/v1/orders")
        self.assertEqual(response.status_code, 204)

    def test_wrong_orderId(self):
        response = self.client.get("/api/v1/orders/a")
        self.assertEqual(response.status_code, 400)

    def test_missing_input_field_in_orders(self):
        order = {
           "amount": "2",
           "food": "1"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_missing_input_field_in_menu(self):
        menu = {
           "name": "chicken"
        }
        response = self.client.post("/api/v1/menu", data = json.dumps(menu), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)

    def test_strip_trailing_spaces_from_orders_posted(self):
        order = {
            "name": "    jon doe  ",
            "amount": "     4   ",
            "food": "3"
        }
        post_order = Order()
        response = self.client.post("/api/v1/orders", data = json.dumps(order), content_type = 'application/json')
        self.assertEqual(post_order.ORDER[2]["name"], "jon doe")
        self.assertEqual(post_order.ORDER[2]["amount"], "4")
        self.assertEqual(post_order.ORDER[2]["food"], 3)
    
    def test_strip_trailing_spaces_from_menu_posted(self):
        menu = {
            "name": "     rice     ",
            "price":     3000
        }
        response = self.client.post("/api/v1/menu", data = json.dumps(menu), content_type = 'application/json')
        menu = Menu()
        self.assertEqual(menu.MENU[1]["name"], "rice")
        self.assertEqual(menu.MENU[1]["price"], 3000)