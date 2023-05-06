#!/usr/bin/python3
"""a python script that displays the X-Request-Id"""
import urllib.request
from sys import argv

if len(argv) > 1:
    url_req = argv[1]
    url = urllib.request.Request(url_req)
    with urllib.request.urlopen(url) as html:
        content = html.getheader("X-Request-Id")
        print(content)
