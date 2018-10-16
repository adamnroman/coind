#!/usr/local/bin python3
from src import omnibus

if __name__ == '__main__':
    omnibus.run(host='127.1', port=5001, debug=True)