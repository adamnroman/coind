#!/usr/local/bin python3

from run.src.models.orm import Database

with Database('dealbase.db') as db:
    db.execute("""CREATE TABLE IF NOT EXISTS users(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR,
                password VARCHAR,
                email VARCHAR);""")
    db.execute("""CREATE TABLE IF NOT EXISTS original(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR,
                product VARCHAR,
                price INTEGER,
                percentage INTEGER,
                url VARCHAR,
                image VARCHAR,
                status VARCHAR,
                date TEXT);""")
    db.execute("""CREATE TABLE IF NOT EXISTS data(
               pk INTEGER PRIMARY KEY AUTOINCREMENT,
               username VARCHAR,
               product VARCHAR,
               url VARCHAR,
               price INTEGER,
               date TEXT);""")
