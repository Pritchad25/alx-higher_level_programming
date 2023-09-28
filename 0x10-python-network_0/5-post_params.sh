#!/bin/bash
#This Bash script takes in a URL, sends a POST request to it, and then displays the body of the response
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -s "$1"
