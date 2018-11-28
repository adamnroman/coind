#!/usr/bin/env python3

from .orm import Database

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

import requests
from bs4 import BeautifulSoup


def insert_url(user, product, url, percentage):
    with Database('dealbase.db') as db:
        db.execute("SELECT * FROM original WHERE username = '{}' AND product = '{}';".format(user, product))
        results = db.fetchall()
        print(results)
        if len(results) != 0:
            return 'FAILED'
        price, image, status = ebay_getprice(url)
        db.execute("""INSERT INTO original(username, product, price, percentage, url, image, status, date) VALUES('{}', '{}', {}, {}, '{}', '{}', '{}', date('now'));""".format(user, product, price, percentage, url, image, status))
    return 'SUCCESS'


def ebay_getprice(url):
    headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}, 
                {'User-Agent': 'Chrome/33.0.1750.117'}, {'User-Agent': 'Safari/537.36'}]
    header = random.choice(headers)
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find(id="prcIsum")
    if not price or price == '':
        price = soup.find(class_="notranslate")
    pricestr = price.text
    index = pricestr.find('$')
    index2 = pricestr.rfind(' ')
    print(pricestr)
    try:
        priceval = float(pricestr[index+1:])
    except:
        priceval = float(pricestr[index+1:index2])
    try:
        image = soup.find(id='icImg')['src']
    except:
        image = "https://www.bullionbypost.co.uk/media/uploads/images/2015/04/21/jqb_0468.JPG"
    try:
        status = soup.find(id="vi-itm-cond")
        status = status.text
    except:
        status = "Probably new..."
    return priceval, image, status

