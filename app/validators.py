from app import app
from flask import request, jsonify
import re
from pyisemail import is_email
from werkzeug.security import generate_password_hash, check_password_hash


class Validators:

    def validate_empty_space(self, order):
        for k in order:
            if order[k].isspace():
                return True
        else:
            return False

    def return_missing_field(self, missing_field):
        missing = ''
        for field in missing_field:
            missing += field + ', '
        return missing

    def validate_input(self, order, required_fields):
        match_name = re.compile(r"^[a-zA-Z0-9 ]+$")
        match_amount = re.compile(r"[0-9]+")
        if not match_amount.search(required_fields[0]) or not match_amount.search(
                required_fields[1]):
            return True
        return False

    def validate_account_input(self, order):
        match_name = re.compile(r"^[a-zA-Z0-9 ]+$")
        if not match_name.search(order["name"]) or not match_name.search(
                order["username"]) or not is_email(order["email"]):
            return True
        return False

    def validate_login_input(self, login):
        match_name = re.compile(r"^[a-zA-Z0-9 ]+$")
        if not match_name.search(login["username"]):
            return True
        return False

    def strip_input(self, order):
        for k, v in order.items():
            if isinstance(order[k], str):
                order[k] = v.strip()
        return order

    def validate_missing(self, order, required_order):
        missing = []
        for k in required_order:
            if order.get(k) == None:
                missing.append(k)
                
            return missing

    def return_key(self, order_status):
        key_order_status = ["New", "Processing", "Cancelled", "Complete"]
        for k in key_order_status:
            if k == order_status:
                return True
        else:
            return False

    def unhash_password(self, hashed_password, login_password):
        return check_password_hash(hashed_password["password"],
                                   login_password["password"])

    def instance_of_post(self, account):
        instance = []
        for k in account:
            if not isinstance(account[k], str):
                instance.append(k)
        return instance
