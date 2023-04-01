#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == '__main__':
    rv = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
          type(rv.text), rv.text))
