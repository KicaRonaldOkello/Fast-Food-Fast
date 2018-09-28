"""Handles how to store and retrieve data."""
#from app import app

class Menu:
    """Class to handle all actions on menu object."""
    MENU = []
    def add_menu_item(self, menu):
        """Method to add items to menu list."""
        menu["food_id"] = (len(self.MENU) + 1)
        self.MENU.append(menu)
        return menu

    def get_menu(self):
        """Returns all items in the menu list."""
        return self.MENU

    def food_name(self, ids):
        """Returns food name after taking its id."""
        for food_id in self.MENU:
            if food_id["food_id"] == ids:
                return food_id["name"]

class Order(Menu):
    """Handles all actions of ordering."""
    ORDER = []
    def add_orders(self, order):
        """Adds orders to the order list."""
        order["order_no"] = (len(self.ORDER) + 1)
        order["order_status"] = "Pending"
        for k, v in order.items():
            if k == "food":
                order[k] = int(v)
        self.ORDER.append(order)
        return order

    def get_orders(self):
        """Returns all orders in the order list."""
        ORDERS = self.ORDER[:]
        for food in ORDERS:
            if isinstance(food["food"], int):
                food_names = self.food_name(food["food"])
                food["food"] = food_names
        return ORDERS  

    def get_an_order(self, orderId):
        """Returns a specific order from the order list."""
        ORDERS = self.ORDER[:]
        one_order = [order for order in ORDERS if order["order_no"] == orderId]
        if isinstance(one_order[0]["food"], int):
            food_name = self.food_name(one_order[0]["food"])
            one_order[0]["food"] = food_name
        return one_order

    def get_length(self, orderId):
        one_order = [order for order in self.ORDER if order["order_no"] == orderId]
        return one_order

    def update_order_status(self, orderId, order_status):
        """Updates the status of an order."""
        update_order = [status for status in self.ORDER if status["order_no"] == orderId]
        if update_order:
            update_order[0]["order_status"] = order_status
            return update_order
        else:
            return "does not exist"

