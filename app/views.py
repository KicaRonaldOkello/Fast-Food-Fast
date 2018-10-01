"""Handles all the views of the application."""
from app import app
from flask import request, jsonify, make_response
from app.models import Database
from app.validators import Validators
from app.dboperations import Order,Menu

orders = Order()
menus = Menu()
db=Database()
db.create_menu_table()
db.create_user_table()
db.create_orders_table()
validator = Validators()

@app.route("/api/v1/orders", methods=["POST"])
def add_order():
    """Implements the add order api."""
    missing_field = validator.validate_post_missing(request.json)
    if missing_field:
        return jsonify({"Error": "Missing field"}), 400
    order = {
        "amount": request.json["amount"],
        "food": request.json["food"]
    }
    empty_space = validator.validate_empty_space(order)
    if empty_space:
        return jsonify({"Error": "Incomplete order"}), 400

    inputs = validator.validate_input(order)
    if inputs:
        return jsonify({"error": "One or all of the keys is taking invlaid input"}), 400
    else:
        stripped_data = validator.strip_input(order)

        orders.add_orders(stripped_data,user_id=1)
        return jsonify({'order': order}), 201

@app.route("/api/v1/menu", methods=["POST"])
def add_menu():
    """Implements the add menu api."""
    validate_missing = validator.validate_missing_menu(request.json)
    if validate_missing:
        return jsonify({"Error": "Missing input field"}), 400
    menu = {
        "name": request.json["name"],
        "price": request.json["price"]
    }
    empty_space = validator.validate_empty_space(menu)
    if empty_space:
        return jsonify({"Error": "Incomplete menu item"}), 400

    strip = validator.strip_input(menu)

    check_for_duplicate = menus.check_duplicate(strip)

    if not check_for_duplicate:
        menus.add_menu_item(strip)
        return jsonify({'menu': menu}), 201
    else:
        return jsonify({"Error": "Menu item already exists"}), 409

    

@app.route("/api/v1/menu", methods=["GET"])
def get_all_menu():
    """Implements the get menu api."""
    menu_items = menus.get_menu()
    return jsonify({'menu': menu_items}), 200

@app.route("/api/v1/orders", methods=["GET"])
def get_all_orders():
    """Implements the get orders api."""
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
    order_status = request.json["status"]
    if  not orderId.isdigit():
        return jsonify({"Error": "Please input correct order id"}), 400

    key_input = validator.return_key(order_status)
    if not key_input:
        return jsonify({"Error": "Wrong key word"}), 400
        
    one_order = orders.get_length(int(orderId))
    if one_order:
        
        updated = orders.update_order_status(int(orderId), order_status)
        return jsonify({"order": updated}), 201
    else:
        return jsonify({"Error": "Order does not exist"}), 404

