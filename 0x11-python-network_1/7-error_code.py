#!/usr/bin/python3
"""
This Python script takes in a URL, sends a request to it and
displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])

    if res.status_code >= 400:
        print('Error code:', res.status_code)
    else:
        print(res.text)
