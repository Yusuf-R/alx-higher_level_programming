#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request
to the URL and displays the value of the variable
"""
import requests
from sys import argv


if __name__ == '__main__':
    rv = requests.get(argv[1])
    print(rv.headers.get('x-Request-Id'))
