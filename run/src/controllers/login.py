#!/usr/local/bin python3

from flask import Blueprint, render_template, request, session
from ..models import login

controller = Blueprint('login', __name__)

@controller.route('/', methods=['GET','POST'])
def log_in():
    if 'username' in session:
        return redirect('/homepage')
    else:
        if request.method == 'GET':
            return render_template('login.html')
        else:
            #Don't want to create a session until the username and password match a user
            username = request.form['username']
            password = request.form['password']
            return login.login(username,password)
