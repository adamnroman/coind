#!/usr/bin/env python3

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
        db.execute("""INSERT INTO original(username, product, price, percentage, url, date) VALUES('{}', '{}', {}, {}, '{}', date('now'));""".format(user, product, price, percentage, url))
    return 'SUCCESS'


def ebay_getprice(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find(class_="notranslate")
    pricestr = price.text
    index = pricestr.find('$')
    priceval = float(pricestr[index+1:])
    return priceval

