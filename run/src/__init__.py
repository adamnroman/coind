#!/usr/local/bin python3

from flask import Flask
import uuid

from .controllers.login import controller as login_controller
from .controllers.create_user import controller as create_user_controller


omnibus = Flask(__name__)
omnibus.secret_key = str(uuid.uuid4())

omnibus.register_blueprint(login_controller)
omnibus.register_blueprint(create_user_controller)