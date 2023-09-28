#!/bin/bash
#This Bash script takes in a URL and displays all HTTP methods that will be accepted by the server.
curl -I -X OPTIONS -s "$1" | grep "Allow:" | sed 's/Allow: //'
