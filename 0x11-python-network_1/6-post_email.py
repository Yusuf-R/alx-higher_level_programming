#!/usr/bin/python3
"""displays the body of the response"""
import requests
from sys import argv


if __name__ == '__main__':
    rv = requests.post(argv[1], data={'email': argv[2]})
    print(rv.text)
