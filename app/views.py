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
        "food_id": request.json["food_id"]
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
