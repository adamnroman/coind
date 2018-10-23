#!usr/bin/env python3

from .orm import Database

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import requests
from bs4 import BeautifulSoup


def insert_url(user, product, url, percentage):
    with Database('dealbase.db') as db:
        db.execute("SELECT * FROM original WHERE username = '{}' AND product = '{}';".format(user, product))
        results = db.fetchall()
        print(results)
        if len(results) != 0:
            return 'FAILED'
        price = ebay_getprice(product)
        db.execute("""INSERT INTO original(username, product, price, url, percentage) VALUES('{}', '{}', {}, '{}', {});""".format(user, product, price, url, percentage))
    return 'SUCCESS'


def ebay_getprice(url):
    page = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=fluent+python&_sacat=0&LH_ItemCondition=3&rt=nc&LH_BIN=1")
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find(class_="s-item__price")
    pricestr = price.text
    priceval = float(pricestr[1:])
    return priceval
