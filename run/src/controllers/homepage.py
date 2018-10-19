from flask import Blueprint, render_template, request, session, redirect
from ..models import homepage

controller = Blueprint('homepage', __name__)

@controller.route('/homepage', methods=['POST','GET'])
def home():
    if 'username' in session:
        if request.method == 'POST':
            return render_template('homepage.html')
        else:
            return render_template('homepage.html')
    else:
        return redirect('/')