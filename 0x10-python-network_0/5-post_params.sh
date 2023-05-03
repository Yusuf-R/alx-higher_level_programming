#!/bin/bash
#Send a POST request to a URL with email and subject variables
curl -s -X POST -H "Content-Type: application/json" -d '{"email":"test@gmail.com","subject":"I will always be here for PLD"}' "$1"
