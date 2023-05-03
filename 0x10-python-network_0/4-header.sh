#!/bin/bash
# script that takes in a URL and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
