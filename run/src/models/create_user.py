#!/usr/bin/env python3
from .orm import Database
from flask import redirect, url_for, render_template, session

def create_login(username,password):
    with Database('database.db') as db:
        db.execute("""INSERT INTO users(username,password) VALUES('{}','{}');""".format(username,password))
        session['username'] = username
        return redirect('/homepage')

def check_db(username,password):
    with Database('database.db') as db:
        db.execute("""SELECT * FROM users WHERE username=?;""",(username,))
        check = db.fetchall()
        if check:
            return render_template('create_user.html', test="User already exists in database")
        else:
            return create_login(username,password)
