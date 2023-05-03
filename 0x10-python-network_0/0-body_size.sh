#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response

err_msg="Usage: <./script.sh> URL"
# Check if URL argument was provided
if [ -z "$1" ]; then
  echo "$err_msg"
  exit 1
fi

# Send request and display size of body
curl -s -w '%{size_download}\n' -o /dev/null "$1"
