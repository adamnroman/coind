from flask import Blueprint, render_template, request, session, redirect
from ..models import homepage

controller = Blueprint('homepage', __name__)

@controller.route('/homepage', methods=['POST','GET'])
def home():
    if 'username' in session:
        if request.method == 'POST':
            product = request.form['product']
            x_data, y_data = homepage.generate_data(product)
            plot_url = homepage.generate_graph(x_data, y_data, product)
            return render_template('homepage.html', product = product)
        else:
            return render_template('homepage.html')
    else:
        return redirect('/')