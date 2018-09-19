from app import app
from flask import jsonify

class Order:
    ORDER = []
    def add_orders(self, order):
        order["order_no"] = (len(self.ORDER) + 1)
        self.ORDER.append(order)
        return order
        
class Menu:
    MENU = []
    def add_menu_item(self, menu):
        menu["food_id"] = (len(self.MENU) + 1)
        self.MENU.append(menu)
        return menu
