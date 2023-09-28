#!/bin/bash
#This Bash script takes in a URL as an argument and then sends a GET request to the it. And then displays the body of the response
curl -X GET -H "X-School-User-Id:98" -s "$1"
