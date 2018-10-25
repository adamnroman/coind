from flask import Flask, Blueprint, render_template, request, session, abort, redirect
import time
from ..models import track, homepage

controller = Blueprint('track', __name__)


@controller.route('/add-product', methods=['GET', 'POST'])
def trackfnc():
    if 'username' in session:
        time1 = time.time()
        username = session['username']
        if request.method == 'POST':
            productname = request.form['product']
            percentage = request.form['percentage']
            print(track.insert_product(username, productname, percentage))
            time2 = time.time()
            print(str(time2-time1) + 'seconds taken')
            return redirect('/homepage')
        return render_template('productinput.html', info=homepage.get_table_info(username))
    else:
        abort(403)