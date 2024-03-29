#!/usr/bin/python3
"""
script that takes username and PAT
and displays the id of the user
"""
import requests
from sys import argv

if __name__ == "__main__":
    usr = argv[1]
    paswd = argv[2]
    url = "https://api.github.com/user"

    html = requests.get(url, auth=(usr, paswd))
    try:
        html_json = html.json()
        if html_json:
            print("{}".format(html_json.get("id")))
    except ValueError:
        print("Not a valid JSON")
