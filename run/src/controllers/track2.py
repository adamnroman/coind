from flask import Flask, Blueprint, render_template, request, session, abort, redirect
import time
from ..models import track, homepage

controller = Blueprint('track2', __name__)


@controller.route('/track_product', methods=['GET', 'POST'])
def track_product():
    if request.method == 'GET':
        return render_template('track.html')