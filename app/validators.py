from app import app
from flask import request, jsonify
import re
class Validators:
    def validate_post_missing(self,order):
        if order.get(
            "name") == None or order.get("amount") == None or order.get("food") == None:
            return True
        else:
            return False
            
    def validate_empty_space(self, order):
        for k in order:
            if order[k].isspace():
                return True
        else:
            return False
        
    def validate_input(self, order):
        match_name = re.compile(r"^[a-zA-Z0-9 ]+$")
        match_amount = re.compile(r"[0-9]+")
        if not match_name.search(order["name"]) or not match_amount.search(
            order["amount"]) or not match_amount.search(order["food"]):
            return True
        return False
            
    def strip_input(self,order):
        for k, v in order.items():
            if isinstance(order[k], str):
                order[k] = v.strip()   
        return order

    def validate_missing_menu(self,order):
        if request.json.get("name") == None or request.json.get("price") == None:
            return True
        else:
            return False
        