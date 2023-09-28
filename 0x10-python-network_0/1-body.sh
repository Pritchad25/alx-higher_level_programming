#!/bin/bash
#This Bash script takes in a URL, sends a GET request to it, and displays the body of the response.
curl -s -o /dev/null -w "%{http_code}" "$1" | [ "$(cat)" == "200" ] && curl -s "$1"
