#!usr/bin/env python3

from .orm import Database

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import requests
from bs4 import BeautifulSoup


def insert_product(user, product):
    with Database('dealbase.db') as db:
        db.execute("SELECT * FROM productstorage WHERE username = '{}' AND product = '{}';".format(user, product))
        results = db.fetchall()
        print(results)
        if len(results) != 0:
            return 'FAILED'
        originalprice = ebayfnc(product)
        db.execute("""INSERT INTO productstorage(username, product, originalprice, url) VALUES('{}', '{}', {}, '{}');""".format(user, product, originalprice, 'abc'))
    return 'SUCCESS'


def ebayfnc(productname):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://www.ebay.com")
    elem = driver.find_element_by_id("gh-ac")
    elem.clear()
    elem.send_keys(productname)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    page = requests.get(driver.current_url)
    driver.close()
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find(class_="s-item__price")
    pricestr = price.text
    priceval = float(pricestr[1:])
    return priceval