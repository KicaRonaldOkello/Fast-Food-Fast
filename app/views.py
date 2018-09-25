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
    if order["name"] == "" or order["amount"] == "" or order["food"] == "":
        return jsonify({"Error": "Incomplete order"}), 400
        
    else:
        orders.add_orders(order)
        return jsonify({'order': order }), 201

@app.route("/api/v1/menu", methods = ["POST"])
def add_menu():
    menu = {
        "name": request.json["name"],
        "price": request.json["price"]
    }
    duplicate = [item for item in menus.MENU if item["name"] == menu["name"]]
    if menu["name"] == "" or menu["price"] == "":
        return jsonify({"Error": "Incomplete menun item"}), 400
    if not duplicate:
        menus.add_menu_item(menu)
        return jsonify({'menu': menu}), 201
    else:
        return jsonify({"Error": "Menu item already exists"}), 409

@app.route("/api/v1/menu", methods = ["GET"])
def get_all_menu():
    if menus.MENU == []:
        return jsonify({"menu": "no menu items"}), 204
    else:
        menu_items = menus.get_menu()
        return jsonify({'menu': menu_items}), 200

@app.route("/api/v1/orders", methods = ["GET"])
def get_all_orders():
    if orders.ORDER == []:
        return jsonify({"order": "no orders"}), 204
    order_list = orders.get_orders()
    return jsonify({'orders': order_list}), 200

@app.route("/api/v1/orders/<int:orderId>", methods = ["GET"])
def get_one_order(orderId):
    if isinstance(orderId,int):
        one_order = orders.get_an_order(orderId)
        return jsonify({"order": one_order}),200
    else:
        return jsonify({"Error": "Please input correct order id"}), 400

@app.route("/api/v1/orders/<orderId>", methods = ["PUT"])
def update_order(orderId):
    order_status = request.json["status"]
    updated = orders.update_order_status(int(orderId), order_status)
    return jsonify({"order": updated}), 201

