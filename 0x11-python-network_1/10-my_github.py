#!/usr/bin/python3
"""GitHub credentials API to display id"""
import requests
from sys import argv


if __name__ == '__main__':
    rv = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        print(rv.json().get('id'))
    except ValueError:
        print('Not a valid JSON')
