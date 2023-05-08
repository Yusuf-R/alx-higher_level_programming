#!/usr/bin/python3
"""
script that takes repo name and owner and display the first
10 commits of the repo in the form <"sha"> <"name">
"""
import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]
    url = ("https://api.github.com/repos/{}/{}/commits"
           .format(owner_name, repo_name))
    html = requests.get(url)
    html_body = html.json()
    iter = 0
    for keys in html_body:
        if iter < 10:
            print("{}: {}".format(
                keys.get("sha"),
                keys.get("commit").get("author").get("name")))
        iter += 1
