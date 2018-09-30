"""Handles how to store and retrieve data."""
from app import app
import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=FastFoodFast user=postgres password=password host=localhost")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        print("Connected to the database")

    def create_user_table(self):
        user_table = ("CREATE TABLE IF NOT EXISTS users"
                    "(user_id serial  NOT NULL PRIMARY KEY,"
                    "name VARCHAR(50) NOT NULL,"
                    "username VARCHAR(50) UNIQUE NOT NULL,"
                    "email VARCHAR(80) UNIQUE NOT NULL,"
                    "password VARCHAR(200) NOT NULL)")

        self.cur.execute(user_table)

    def create_menu_table(self):
        menu_table = ("CREATE TABLE IF NOT EXISTS menu"
                        "(menu_id serial NOT NULL PRIMARY KEY,"
                        "food_name VARCHAR(60) UNIQUE NOT NULL,"
                        "price INTEGER NOT NULL)")
        self.cur.execute(menu_table)

    def create_orders_table(self):
        orders_table = ("CREATE TABLE IF NOT EXISTS orders"
                        "(order_id serial  NOT NULL PRIMARY KEY,"
                        "amount INTEGER NOT NULL,"
                        "time TIMESTAMP NOT NULL,"
                        "order_status VARCHAR(11) NOT NULL,"
                        "user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(user_id),"
                        "menu_id INTEGER, FOREIGN KEY (menu_id) REFERENCES menu(menu_id))")
        self.cur.execute(orders_table)


