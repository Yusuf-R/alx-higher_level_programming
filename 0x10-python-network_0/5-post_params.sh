#!/bin/bash
#Send a POST request to a URL with email and subject variables
curl -s -X POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1" # & also works instead of repeating -d
