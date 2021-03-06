#!/usr/local/bin python3

from flask import Flask
import uuid

from .controllers.login import controller as login_controller
from .controllers.create_user import controller as create_user_controller
from .controllers.track import controller as track_controller
from .controllers.homepage import controller as home_controller
from .controllers.url import controller as url_controller
from .controllers.logout import controller as logout_controller
from .controllers.track2 import controller as track2_controller
from .controllers.remove import controller as remove_controller


omnibus = Flask(__name__)
omnibus.secret_key = str(uuid.uuid4())

omnibus.register_blueprint(login_controller)
omnibus.register_blueprint(create_user_controller)
omnibus.register_blueprint(track_controller)
omnibus.register_blueprint(url_controller)
omnibus.register_blueprint(home_controller)
omnibus.register_blueprint(logout_controller)
omnibus.register_blueprint(track2_controller)
omnibus.register_blueprint(remove_controller)
