#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    my_req = Request(argv[1])
    try:
        with urlopen(my_req) as response:
            rv = response.read()
            print(rv.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
