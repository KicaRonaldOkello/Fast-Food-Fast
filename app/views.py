from app import app
from flask import request, jsonify, make_response
from app.models import Order, Menu

orders = Order()
menus = Menu()

@app.route("/api/v1/orders", methods=["POST"])
def add_order():
    order = {
        "name": request.json["name"],
        "amount": request.json["amount"],
        "food": request.json["food"]
    }
    orders.add_orders(order)
    return make_response(jsonify({'order': order }), 201)

@app.route("/api/v1/menu", methods = ["POST"])
def add_menu():
    menu = {
        "name": request.json["name"],
        "price": request.json["price"]
    }
    menus.add_menu_item(menu)
    return jsonify({'menu': menu}), 201

@app.route("/api/v1/menu", methods = ["GET"])
def get_all_menu():
    menu_items = menus.get_menu()
    return jsonify({'menu': menu_items}), 200

@app.route("/api/v1/orders", methods = ["GET"])
def get_all_orders():
    order_list = orders.get_orders()
    return jsonify({'orders': order_list}), 200

@app.route("/api/v1/orders/<orderId>", methods = ["GET"])
def get_one_order(orderId):
    one_order = orders.get_an_order(orderId)
    return jsonify({"order": one_order}),200

@app.route("/api/v1/orders/<orderId>", methods = ["PUT"])
def update_order(orderId):
    status = orders.update_order_status(orderId)
    return jsonify({"order": status})