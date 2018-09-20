import unittest
from app import app
from app import views
from app.models import Menu
import json

class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_order(self):
        order = {
            'id': 1,
            'name': 'matooke',
            'amount': '15,000',
            'food_id': 2
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_menu(self):
        menu = {
            "id": 1,
            "name": "chicken",
            "price": 2000
        }
        response = self.client.post("/api/v1/menu", data = json.dumps(menu), content_type = 'application/json')
        menu = Menu()
        self.assertEqual(len(menu.MENU), 1)
        self.assertEqual(response.status_code, 201)

    def test_get_menu(self):
        response = self.client.get("/api/v1/menu")
        self.assertEqual(response.status_code, 200)

    def test_get_order(self):
        response = self.client.get("/api/v1/orders")
        self.assertEqual(response.status_code, 200)