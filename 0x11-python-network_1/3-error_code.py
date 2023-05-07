#!/usr/bin/python3
"""displays the body of the response and handles exceptions"""
import urllib.request
import urllib.error
from sys import argv

if len(argv) > 1:
    url_req = argv[1]

    url = urllib.request.Request(url_req)

    try:
        with urllib.request.urlopen(url) as html:
            html_body = html.read().decode("utf-8")
            print(html_body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
