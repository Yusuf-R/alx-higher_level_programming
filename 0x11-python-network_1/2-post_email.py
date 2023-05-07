#!/usr/bin/python3
"""a python script that displays the X-Request-Id"""
import urllib.request
import urllib.parse
from sys import argv

if len(argv) > 2:
    url_req = argv[1]
    email = argv[2]
    info = {"email": email}

    data = urllib.parse.urlencode(info).encode("ascii")
    url = urllib.request.Request(url_req, data=data, method="POST")

    with urllib.request.urlopen(url) as html:
        html_body = html.read().decode("utf-8")
        print(html_body)
