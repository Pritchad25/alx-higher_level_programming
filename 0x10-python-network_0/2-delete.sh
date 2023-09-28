#!/bin/bash
#This Bash script sends a DELETE request to the URL passed as the first argument. And then displays the body of the response.
curl -s -X DELETE "$1"
