#!/bin/bash
# display only the http_code of the response header
curl -s -w '%{status_code}' -o /dev/null "$1"
