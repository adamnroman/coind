#!/usr/local/bin python3

from flask import Blueprint, render_template, request, redirect, session
from ..models import create_user

controller = Blueprint('create_user',__name__)

@controller.route('/create_user', methods=['GET','POST'])
def newUser():
    if 'username' not in session:
        if request.method == 'POST':
            #TODO stuff
            username = request.form['username']
            password = request.form['password']
            password2 = request.form['password2']
            if password==password2:
                return create_user.check_db(username,password)
            else:
                return render_template('create_user.html',test='Passwords do not match')
            
        else:
            return render_template('create_user.html')
    else:
        return redirect('/homepage')