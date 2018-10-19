#!/usr/local/bin python3
from .orm import Database
from flask import render_template, session, redirect
import sqlite3

def login(username,password):
    #check username
    with Database('dealbase.db') as db:
        db.execute("""SELECT password FROM users WHERE username=?;""",(username,))
        db_password = db.fetchone()
        if db_password:
            #username does exist in database
            if db_password[0] == password:
                #passwords match
                session['username'] = username
                return redirect('/homepage')
            else:
                return render_template('login.html', message="Incorrect Password")

        else:
            #username doesn't exist in database
            return render_template('login.html', message="User does not exist.", message_link='<a class="btn btn-secondary" href="/create_user" role="button">Create new user?</a>')

