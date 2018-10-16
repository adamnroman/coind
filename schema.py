#!/usr/local/bin python3

from run.src.models.orm import Database

with Database('database.db') as db:
    db.execute("""CREATE TABLE IF NOT EXISTS users(
               username VARCHAR,
               password VARCHAR);"""
               )
    