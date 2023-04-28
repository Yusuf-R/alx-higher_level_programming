#!/bin/bash
# script that sends a DELETE request to the URL passedas the first argument and displays the body of the response
curl -sI $1 | grep Allow | cut -d ' ' -f2-
