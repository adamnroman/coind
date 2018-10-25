from flask import Blueprint, render_template, request, session, redirect
from ..models import homepage
import os

controller = Blueprint('homepage', __name__)

@controller.route('/homepage', methods=['POST','GET'])
def home():
    if 'username' in session:
        username = session['username']
        info = homepage.get_table_info(username)
        if request.method == 'POST':
            product = request.form['product']
            x_data, y_data = homepage.generate_graph_data(product)
            info = homepage.get_table_info(username)
            if len(y_data) > 1:
                #generates the graph and returns the time key for file naming
                time_string = homepage.generate_graph(x_data, y_data, product)
                return render_template('homepage.html', product = product+time_string, info=info)
            else:
                return render_template('homepage.html', info=info, response= "Not enough data to represent accurate trends. Please try again later.")
        else:
            return render_template('homepage.html',info=info)
    else:
        return redirect('/')