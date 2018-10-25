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
               'http://www.toy.com',
               5,
               datetime('now'));"""   
               )
    db.execute("""INSERT INTO data(
               username,
               product,
               url,
               price,
               date) VALUES(
               'adam',
               'toy',
               'http://www.toy.com',
               23,
               '2018-10-26');"""   
               )
    db.execute("""INSERT INTO data(
               username,
               product,
               url,
               price,
               date) VALUES(
               'adam',
               'toy',
               'http://www.toy.com',
               10,
               '2018-10-25');"""   
               )
    db.execute("""INSERT INTO original(
                username,
                product,
                price,
                percentage,
                url,
                date) VALUES(
                'adam',
                'toy',
                25,
                10,
                'http://www.toy.com',
                '2018-10-22');"""
    )
    db.execute("""INSERT INTO original(
                username,
                product,
                price,
                percentage,
                url,
                date) VALUES(
                'adam',
                'toy2',
                300,
                25,
                'http://www.toy.com',
                '2018-10-15');"""
    )