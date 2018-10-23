from flask import Flask, Blueprint, render_template, request, session, abort
import time
from ..models import url

controller = Blueprint('url', __name__)


@controller.route('/add-url', methods=['GET', 'POST'])
def urlfnc():
    if 'username' in session:
        time1 = time.time()
        username = session['username']
        if request.method == 'POST':
            product = request.form['product']
            urlval = request.form['url']
            percentage = request.form['percentage']
            print(url.insert_url(username, product, urlval, percentage))
            time2 = time.time()
            print(str(time2-time1) + 'seconds taken')
            return render_template('urlinput.html')
        return render_template('urlinput.html')
    else:
        abort(403)