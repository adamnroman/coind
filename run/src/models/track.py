#!usr/bin/env python3

from .orm import Database

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

import requests
from bs4 import BeautifulSoup


def insert_product(user, product, percentage):
    with Database('dealbase.db') as db:
        db.execute("SELECT * FROM original WHERE username = '{}' AND product = '{}';".format(user, product))
        results = db.fetchall()
        print(results)
        if len(results) != 0:
            return 'FAILED'
        originalprice, url, image_url, status = ebayfnc(product)
        db.execute("""INSERT INTO original(username, product, price, percentage, url, image, status, date) VALUES(?,?,?,?,?,?,?, datetime('now'));""",(user, product, originalprice, percentage, url, image_url, status))
        db.execute("""INSERT INTO data(username, product, url, price, date) VALUES(?,?,?,?,datetime('now'));""",(user, product, url, originalprice))
    return 'SUCCESS'


def ebayfnc(productname):
    driver = webdriver.Chrome('chromedriver')
    driver.get("http://www.ebay.com")
    elem = driver.find_element_by_id("gh-ac")
    elem.clear()
    elem.send_keys(productname)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}, 
               {'User-Agent': 'Chrome/33.0.1750.117'}, {'User-Agent': 'Safari/537.36'}]
    header = random.choice(headers)
    page = requests.get(driver.current_url, headers=header)
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find(class_="s-item__price")
    if not price or price == ' ' or price == []:
        price = soup.find(id="prcIsum")
    try:
        pricestr = price.text
        priceval = float(pricestr[1:])
    except:
        priceval = 0
    try:
        link = driver.find_element_by_class_name('s-item__link')
        link = link.get_attribute("href")
    except:
        link = "No URL Found"
    try:
        image = driver.find_element_by_class_name('s-item__image-img')
        image = image.get_attribute('src')
    except:
        image = "https://www.bullionbypost.co.uk/media/uploads/images/2015/04/21/jqb_0468.JPG"
    try:
        status = soup.find(class_="SECONDARY_INFO")
        status = status.text
    except:
        status = "Probably new..."
    driver.close()
    return priceval, link, image, status
