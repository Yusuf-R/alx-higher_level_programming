#!/usr/bin/python3
"""
   script that takes in a URL and an email address, sends a POST request
   to the passed URL with the email as a parameter, and finally displays
   the body of the response.
"""
import requests
from sys import argv

if len(argv) > 2:
    url = argv[1]
    email = argv[2]
    payload = {"email": email}

    html = requests.post(url, data=payload)
    html_body = html.text
    print(html_body)
