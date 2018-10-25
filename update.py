#!/usr/local/bin python3

##This function will update our database for all the items being tracked. Using Crontab

from run.src.models.orm import Database
from run.src.models.url import ebay_getprice

with Database('dealbase.db') as db:
    db.execute("""SELECT * FROM original;""")
    original_data = db.fetchall()  
    for each in original_data:
        url = each[5]
        price = ebay_getprice(url)
        db.execute("""INSERT INTO data(
                    username,
                    product,
                    url,
                    price,
                    date) VALUES(
                    ?,
                    ?,
                    ?,
                    ?,
                    datetime('now'));""",(each[1], each[2], url, price))
print('done')         


