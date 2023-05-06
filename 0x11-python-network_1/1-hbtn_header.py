#!/usr/bin/python3
"""a python script that fetches a url"""
import urllib.request
from sys import argv
url = argv[1]
with urllib.request.urlopen(url) as response:
    html_header = response.headers
    content = html_header.get("X-Request-Id")
    print(content)
