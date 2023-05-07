#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if len(argv) < 2:
    q = ""
else:
    q = argv[1]

url = "http://0.0.0.0:5000/search_user"
payload = {"q": q}
html = requests.post(url, data=payload)
try:
    html_json = html.json()
    if html_json:
        print("[{}] {}".format(html_json.get("id"), html_json.get("name")))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
