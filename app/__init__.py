from flask import Flask
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

app = Flask(__name__)

from app import views


app.config['JWT_SECRET_KEY'] = 'secret-key'
jwt = JWTManager(app)