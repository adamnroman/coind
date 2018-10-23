#!/usr/local/bin python3

from flask import Blueprint, session, redirect
import os

controller = Blueprint('logout',__name__)

@controller.route('/logout', methods=['GET'])
def logout():
    try:
        os.system('rm /Users/adamroman/Desktop/Byte/coind/run/src/static/graphs/*')
        session.pop('username', None)
        return redirect('/')
    except TypeError:
        return redirect('/')

    