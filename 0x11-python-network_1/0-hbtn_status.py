#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == '__main__':
    my_req = request.Request("https://intranet.hbtn.io/status")
    with request.urlopen(req) as response:
        read_obj = response.read()
        stats = "Body response:\n\t- type: {}\n\t- content: {}"
        stats += "\n\t- utf8 content: {}"
        print(stats.format(type(read_obj), read_obj, read_obj.decode('utf-8')))
