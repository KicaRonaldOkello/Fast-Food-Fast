from app import app
from flask import jsonify

class Order():
    ORDER = []
    def add_orders(self, order):
        order["order_no"] = (len(self.ORDER) + 1)
        self.ORDER.append(order)
        return order

    def get_orders(self):
        ans  = Menu()
        for food in self.ORDER:
            food_names = ans.food_name(food["food"])
            food["food"] = food_names
        return self.ORDER



        
class Menu:
    MENU = []
    def add_menu_item(self, menu):
        menu["food_id"] = (len(self.MENU) + 1)
        self.MENU.append(menu)
        return menu

    def get_menu(self):
        return self.MENU

    def food_name(self, id):
        for food_id in self.MENU:
            if food_id["food_id"] == id:
                return food_id["name"]