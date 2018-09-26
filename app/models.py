from app import app
from flask import jsonify

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

class Order(Menu):
    
    ORDER = []
    def add_orders(self, order):
        
        order["order_no"] = (len(self.ORDER) + 1)
        order["order_status"] = "Pending"
        self.ORDER.append(order)
        return order

    def get_orders(self):
        ORDERS = self.ORDER[:]
        for food in ORDERS:
            if isinstance(food["food"], int):
                food_names = self.food_name(food["food"])
                food["food"] = food_names
        return ORDERS    


    def get_an_order(self, orderId):
        ORDERS = self.ORDER[:]
        one_order = [order for order in ORDERS if order["order_no"] == orderId]
        if isinstance(one_order[0]["food"], int):
            food_name = self.food_name(one_order[0]["food"])
            one_order[0]["food"] = food_name
            return one_order
        else:
            return one_order

    def update_order_status(self, orderId, order_status):
        update_order = [status for status in self.ORDER if status["order_no"] == orderId]
        if update_order:
            update_order[0]["order_status"] = order_status
            return update_order
        else:
            return "does not exist"

    




        
