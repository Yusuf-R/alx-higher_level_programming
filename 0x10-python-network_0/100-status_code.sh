#!/bin/bash
# displays the status code of the http response
curl -s -w '%{http_code}' -o /dev/null "$1"
