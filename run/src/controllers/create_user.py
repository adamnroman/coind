#!/usr/local/bin python3

from flask import Blueprint, render_template, request, redirect, session
from ..models import create_user
import re

controller = Blueprint('create_user',__name__)

@controller.route('/create_user', methods=['GET','POST'])
def newUser():
    if 'username' not in session:
        if request.method == 'POST':
            #TODO stuff
            username = request.form['username']
            password = request.form['password']
            password2 = request.form['password2']
            email = request.form['email']
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return render_template('create_user.html', test='Enter a valid email')
            if password==password2:
                return create_user.check_db(username,password,email)
            else:
                return render_template('create_user.html',test='Passwords do not match')
            
        else:
            return render_template('create_user.html')
    else:
        return redirect('/homepage')