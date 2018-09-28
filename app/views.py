"""Handles all the views of the application."""
from app import app
from flask import request, jsonify, make_response
from app.models import Order, Menu
import re

orders = Order()
menus = Menu()

@app.route("/api/v1/orders", methods=["POST"])
def add_order():
    """Implements the add order api."""
    if request.json.get(
            "name") == None or request.json.get("amount") == None or request.json.get("food") == None:
            return jsonify({"Error": "Missing field"}), 400
    order = {
        "name": request.json["name"],
        "amount": request.json["amount"],
        "food": request.json["food"]
    }
    if order["name"].isspace() or order["amount"].isspace() or order["food"].isspace():
        return jsonify({"Error": "Incomplete order"}), 400

    match_name = re.compile(r"^[a-zA-Z0-9 ]+$")
    match_amount = re.compile(r"[0-9]+")
    if not match_name.search(order["name"]) or not match_amount.search(
        order["amount"]) or not match_amount.search(order["food"]):
        return jsonify({"error": "One or all of the keys is taking invlaid input"}), 400
    else:
        for k, v in order.items():
            if isinstance(order[k], str):
                order[k] = v.strip()   
        orders.add_orders(order)
        return jsonify({'order': order}), 201

@app.route("/api/v1/menu", methods=["POST"])
def add_menu():
    """Implements the add menu api."""
    if request.json.get("name") == None or request.json.get("price") == None:
        return jsonify({"Error": "Missing input field"}), 400
    menu = {
        "name": request.json["name"],
        "price": request.json["price"]
    }
    duplicate = [item for item in menus.MENU if item["name"] == menu["name"]]
    if menu["name"] == "" or menu["price"] == "":
        return jsonify({"Error": "Incomplete menun item"}), 400
    if not duplicate:
        for k, v in menu.items():
            if isinstance(menu[k], str):
                menu[k] = v.strip()

        menus.add_menu_item(menu)
        return jsonify({'menu': menu}), 201
    else:
        return jsonify({"Error": "Menu item already exists"}), 409

    

@app.route("/api/v1/menu", methods=["GET"])
def get_all_menu():
    """Implements the get menu api."""
    if menus.MENU == []:
        return jsonify({"menu": "no menu items"}), 204
    else:
        menu_items = menus.get_menu()
        return jsonify({'menu': menu_items}), 200

@app.route("/api/v1/orders", methods=["GET"])
def get_all_orders():
    """Implements the get orders api."""
    if orders.ORDER == []:
        return jsonify({"order": "no orders"}), 204
    order_list = orders.get_orders()
    return jsonify({'orders': order_list}), 200

@app.route("/api/v1/orders/<orderId>", methods=["GET"])
def get_one_order(orderId):
    """Implements api to get a specific order."""
    if  not orderId.isdigit():
        return jsonify({"Error": "Please input correct order id"}), 400

    one_order = orders.get_length(int(orderId))
    if one_order:
        one_order = orders.get_an_order(int(orderId))
        return jsonify({"order": one_order}), 200

    else:
        return jsonify({"Error": "Order does not exist"}), 404 

@app.route("/api/v1/orders/<orderId>", methods=["PUT"])
def update_order(orderId):
    """Implements api that changes order status."""
    if  not orderId.isdigit():
        return jsonify({"Error": "Please input correct order id"}), 400

    one_order = orders.get_length(int(orderId))
    if one_order:
        order_status = request.json["status"]
        updated = orders.update_order_status(int(orderId), order_status)
        return jsonify({"order": updated}), 201
    else:
        return jsonify({"Error": "Order does not exist"}), 404

