#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL 
and displays the body of the response (decoded in utf-8).
"""
from urllib import request, parse
from sys import argv


if len(argv) > 2:
    email = {'email': argv[2]}
    my_data = parse.urlencode(email).encode('ascii')
    my_req = request.Request(argv[1], my_data)
    with request.urlopen(my_req) as my_resp:
        rv = my_resp.read()
        print(rv.decode('utf-8'))
