from flask import Flask, Blueprint, render_template, request, session, abort
import time
from ..models import track

controller = Blueprint('track', __name__)


@controller.route('/add-product', methods=['GET', 'POST'])
def trackfnc():
    if 'username' in session:
        time1 = time.time()
        username = session['username']
        if request.method == 'POST':
            productname = request.form['product']
            print(track.insert_product(username, productname))
            time2 = time.time()
            print(str(time2-time1) + 'seconds taken')
            return render_template('productinput.html')
        return render_template('productinput.html')
    else:
        abort(403)