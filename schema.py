#!/usr/local/bin python3

from run.src.models.orm import Database

with Database('database.db') as db:
    db.execute("CREATE TABLE IF NOT EXISTS users (pk INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR, password VARCHAR);")
    db.execute("CREATE TABLE IF NOT EXISTS productstorage (pk INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR, product VARCHAR, originalprice INTEGER, url VARCHAR);")
