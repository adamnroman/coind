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
        price = ebay_getprice(url)
        db.execute("""INSERT INTO original(username, product, price, url, percentage) VALUES('{}', '{}', {}, '{}', {});""".format(user, product, price, url, percentage))
    return 'SUCCESS'


def ebay_getprice(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find(class_="notranslate")
    pricestr = price.text
    index = pricestr.find('$')
    priceval = float(pricestr[index+1:])
    return priceval
