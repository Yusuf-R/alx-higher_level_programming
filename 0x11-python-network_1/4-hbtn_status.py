#!/usr/bin/python3
"""a python script that fetches a url using request module"""
import requests

url = "https://alx-intranet.hbtn.io/status"
html = requests.get(url)
content_utf = html.content.decode("utf-8")
print("Body response:")
print("\t- type: {}".format(type(content_utf)))
print("\t- content: {}".format(content_utf))
