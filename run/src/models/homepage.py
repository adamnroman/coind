#!/usr/local/bin python3

import matplotlib.pyplot as plt
from .orm import Database
import sqlite3

def update_database():
    #TODO update the database for the price of the products that the user wants to track
    pass


def generate_data(product):
    #TODO Pulls data from our database and creates a graphable data set out of it
    with Database('dealbase.db') as db:
        #first get x data
        db.execute("""SELECT date FROM data WHERE product=?;""",(product,))
        x_data = db.fetchall()
        # Each piece of x_data is a tuple with the second indexed item not existing. This is fixing that.
        x_data = [each[0] for each in x_data]
        db.execute("""SELECT price FROM data WHERE product=?;""",(product,))
        y_data = db.fetchall()
        y_data = [each_[0] for each_ in y_data]
        return x_data, y_data

def generate_graph(x_data, y_data, product):
    #TODO Uses the compiled data to render a plotly graph
    plt.xlabel('Date')
    plt.ylabel('Price')
    graph = plt.plot(x_data,y_data,label=product)
    plt.savefig('/Users/adamroman/Desktop/Byte/coind/run/src/static/graphs/{}.png'.format(product), dpi = 300)
    