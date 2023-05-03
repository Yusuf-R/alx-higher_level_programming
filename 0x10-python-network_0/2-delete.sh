#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s --request "DELETE" "$1" # you can also use -X flag in place of --request
