#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -i --request OPTIONS "$1" | grep -i "Allow:" | cut -d " " -f 2- # -X flags can also be used
