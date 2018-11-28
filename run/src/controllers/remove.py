from flask import Blueprint, session, redirect, render_template, request, abort
import os
import sqlite3
from ..models.orm import Database
from ..models import homepage

controller = Blueprint('remove',__name__)

@controller.route('/remove', methods=['GET','POST'])
def remove():
    if 'username' in session:
        username = session['username']
        if request.method =='POST':
            product = request.form['product']
            with Database('dealbase.db') as db:
                db.execute("""DELETE FROM original WHERE username=? AND product=?;""",(username,product))
            return redirect('/homepage')
        else:
            return render_template('remove.html', info=homepage.get_table_info(username))
    else:
        abort(403)