#!/usr/bin/python3
"""
This Python script takes in a URL, sends a request to it and
displays the value of the variable X-Request-Id in the
response header
"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])

    if 'X-Request-Id' in res.headers:
        print(res.headers.get('X-Request-Id'))
