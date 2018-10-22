#!/usr/local/bin python3

from run.src.models.orm import Database

with Database('dealbase.db') as db:
    db.execute("""INSERT INTO data(
               username,
               product,
               url,
               price,
               date) VALUES(
               'adam',
               'toy',
               'www.toy.com',
               5,
               date('now'));"""   
               )
    db.execute("""INSERT INTO data(
               username,
               product,
               url,
               price,
               date) VALUES(
               'adam',
               'toy',
               'www.toy.com',
               23,
               date('now'));"""   
               )
    db.execute("""INSERT INTO data(
               username,
               product,
               url,
               price,
               date) VALUES(
               'adam',
               'toy',
               'www.toy.com',
               10,
               date('now'));"""   
               )