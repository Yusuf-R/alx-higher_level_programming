#!/usr/bin/python3
"""displays the X-Request-Id using rquests module"""
import requests
from sys import argv

if len(argv) > 1:
    url = argv[1]
    with requests.get(url) as html:
        content = html.headers.get("X-Request-Id")
        print(content)
