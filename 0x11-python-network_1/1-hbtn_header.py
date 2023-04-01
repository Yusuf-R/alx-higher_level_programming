#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv

if len(argv) > 1:
    with urllib.request.urlopen(argv[1]) as my_resp:
        print(my_resp.getheader("X-Request-Id"))
