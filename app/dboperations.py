from app.models import Database
db = Database()
cursor = db.cur
dictcur = db.dict_cursor
from werkzeug.security import generate_password_hash, check_password_hash


class Menu:
    """Class to handle all actions on menu object."""

    def add_menu_item(self, menu):
        """Method to add items to menu list."""
        for k, v in menu.items():
            if k == "price":
                menu[k] = int(v)

        command = "INSERT INTO menu(food_name, price) VALUES (%s, %s)"
        cursor.execute(command, (menu["name"], menu["price"]))

    def get_menu(self):
        """Returns all items in the menu list."""
        command = "SELECT * FROM menu"
        dictcur.execute(command)
        menu = dictcur.fetchall()
        return menu

    def check_duplicate(self, menu):
        duplicate = "SELECT food_name FROM menu WHERE food_name = '{}'".format(
            menu["name"])
        cursor.execute(duplicate)
        data = cursor.fetchone()
        return data


class Order(Menu):
    """Handles all actions of ordering."""

    def add_orders(self, order, user_id):
        """Adds orders to the order list."""
        for k, v in order.items():
            order[k] = int(v)
        command = "INSERT INTO orders(amount, time, order_status, user_id, menu_id) VALUES(\
        %s, NOW(), %s, %s, %s)"

        cursor.execute(
            command,
            (order["amount"], "New", user_id["user_id"], order["food"]))
        return order

    def get_orders(self):
        """Returns all orders in the order list."""
        command = "SELECT order_id, amount, order_status,time, food_name, username FROM orders \
        INNER JOIN menu ON orders.menu_id = menu.menu_id INNER JOIN users ON orders.user_id = users.user_id"

        dictcur.execute(command)
        data = dictcur.fetchall()
        return data

    def get_an_order(self, orderId):
        """Returns a specific order from the order list."""
        command = "SELECT * FROM orders WHERE order_id ='{}'".format(orderId)
        dictcur.execute(command)
        one_order = dictcur.fetchone()
        return one_order

    def get_order_history(self, user):
        command = "SELECT order_id, amount, order_status,food_name, time FROM orders\
        INNER JOIN menu ON orders.menu_id = menu.menu_id WHERE user_id = '{}'".format(
            user["user_id"])
        dictcur.execute(command)
        order_history = dictcur.fetchall()
        return order_history

    def get_length(self, orderId):
        command = "SELECT order_id FROM orders WHERE order_id ='{}'".format(
            orderId)
        dictcur.execute(command)
        one_order = dictcur.fetchone()
        return one_order

    def update_order_status(self, orderId, order_status):
        """Updates the status of an order."""
        command = "UPDATE orders SET order_status='{}' WHERE order_id ='{}'".format(
            order_status, orderId)
        cursor.execute(command)
        return_order_status = "SELECT * FROM orders WHERE order_id = '{}'".format(
            orderId)
        dictcur.execute(return_order_status)
        data = dictcur.fetchall()
        return data


class Users:
    def check_username(self, account):
        command = "SELECT username,password,role, user_id from users WHERE username= '{}'".format(
            account["username"])
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

    def check_email(self, account):
        command = "SELECT email from users WHERE email= '{}'".format(
            account["email"])
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

    def add_user(self, account):
        command = "INSERT INTO users(name, username, email, password, role) VALUES(\
        '{}', '{}', '{}', '{}', 'user')".format(account["name"], account["username"], account["email"]\
        , generate_password_hash(account["password"]))
        cursor.execute(command)
        return account

    def add_admin(self, account):
        command = "INSERT INTO users(name, username, email, password, role) VALUES(\
        '{}', '{}', '{}', '{}', 'admin')".format(account["name"], account["username"], account["email"]\
        , generate_password_hash(account["password"]))
        cursor.execute(command)
        return_id = "SELECT user_id, username, role FROM users WHERE username = '{}'".format(
            account["username"])
        dictcur.execute(return_id)
        data = dictcur.fetchall()
        return data
