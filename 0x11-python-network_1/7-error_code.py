#!/usr/bin/python3
"""displays the body and the response code if error"""
import requests
from sys import argv

if len(argv) > 1:
    url_req = argv[1]

    url = requests.get(url_req)
    e_code = url.status_code

    if e_code > 399:
        print("Error code: {}".format(e_code))
    else:
        print(url.text)
