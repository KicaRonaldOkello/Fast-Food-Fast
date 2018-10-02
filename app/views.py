"""Handles all the views of the application."""
from app import app
from flask import request, jsonify, make_response
from app.models import Database
from app.validators import Validators
from app.dboperations import Order,Menu,Users
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

orders = Order()
menus = Menu()
user = Users()
db=Database()
db.create_menu_table()
db.create_user_table()
db.create_orders_table()
validator = Validators()

@app.route("/api/v1/orders", methods=["POST"])
@jwt_required
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
@jwt_required
def add_menu():
    """Implements the add menu api."""
    current_user = get_jwt_identity()
    if not current_user["role"] == "admin":
        return jsonify({"Error":"Unauthorised access"}), 401

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
@jwt_required
def get_all_orders():
    """Implements the get orders api."""
    current_user = get_jwt_identity()
    if not current_user["role"] == "admin":
        return jsonify({"Error":"Unauthorised access"}), 401
        
    order_list = orders.get_orders()
    return jsonify({'orders': order_list}), 200

@app.route("/api/v1/orders/<orderId>", methods=["GET"])
@jwt_required
def get_one_order(orderId):
    """Implements api to get a specific order."""
    current_user = get_jwt_identity()
    if not current_user["role"] == "admin":
        return jsonify({"Error":"Unauthorised access"}), 401

    if  not orderId.isdigit():
        return jsonify({"Error": "Please input correct order id"}), 400

    one_order = orders.get_length(int(orderId))
    if one_order:
        one_order = orders.get_an_order(int(orderId))
        return jsonify({"order": one_order}), 200

    else:
        return jsonify({"Error": "Order does not exist"}), 404 

@app.route("/api/v1/orders/<orderId>", methods=["PUT"])
@jwt_required
def update_order(orderId):
    """Implements api that changes order status."""
    current_user = get_jwt_identity()
    if not current_user["role"] == "admin":
        return jsonify({"Error":"Unauthorised access"}), 401

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

@app.route("/api/v1/auth/signup", methods=["POST"])
def create_account():
    validate_missing = validator.validate_missing_account(request.json)
    if validate_missing:
        return jsonify({"Error": "Missing input field"}), 400
    account = {
        "name": request.json["name"],
        "username": request.json["username"],
        "email": request.json["email"],
        "password": request.json["password"]
    }
    empty_space = validator.validate_empty_space(account)
    if empty_space:
        return jsonify({"Error": "Incomplete order"}), 400

    inputs = validator.validate_account_input(account)
    if inputs:
        return jsonify({"error": "One or all of the keys is taking invlaid input"}), 400

    strip = validator.strip_input(account)

    check_for_username = user.check_username(strip)

    if not check_for_username:
        new_account = user.add_user(strip)
        access_token = create_access_token(identity=strip["username"])
        return jsonify(access_token=access_token),201
    else:
        return jsonify({"Error": "Account already exists"}), 409

@app.route("/api/v1/auth/login", methods=["POST"])
def login():
    validate_missing = validator.validate_missing_login(request.json)
    if validate_missing:
        return jsonify({"Error": "Missing input field"}), 400
    login = {
        "username": request.json["username"],
        "password": request.json["password"]
    }
    empty_space = validator.validate_empty_space(login)
    if empty_space:
        return jsonify({"Error": "Incomplete order"}), 400
    
    inputs = validator.validate_login_input(login)
    if inputs:
        return jsonify({"error": "Username is taking invlaid input"}), 400

    strip = validator.strip_input(login)

    check_for_username = user.check_username(strip)
    check_for_password = validator.unhash_password(check_for_username,login)

    if check_for_username and check_for_password:
        access_token = create_access_token(identity=check_for_username)
        return jsonify(access_token=access_token),200
        

    else:
        return jsonify({"Error":"Please input correct username or password"}), 401




    

