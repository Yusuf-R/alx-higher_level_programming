#!/usr/bin/python3
"""a python script that fetches a url"""
import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    html = response.read()
    content_utf = html.decode("utf-8")
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(content_utf))
