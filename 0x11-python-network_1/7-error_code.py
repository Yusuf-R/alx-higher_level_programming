#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response
"""
import requests
from sys import argv


if __name__ == '__main__':
    rv = requests.get(argv[1])
    if rv.status_code >= 400:
        print('Error code:', rv.status_code)
    else:
        print(rv.text)
