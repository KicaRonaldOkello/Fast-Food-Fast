from flask import Flask
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,
                                get_jwt_identity)
from config import DevelopmentConfig
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import views
app.config.from_object(DevelopmentConfig)

app.config['JWT_SECRET_KEY'] = 'secret-key'
jwt = JWTManager(app)
swag = Swagger(app)
