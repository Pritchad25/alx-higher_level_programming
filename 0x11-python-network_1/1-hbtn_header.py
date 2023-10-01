#!/usr/bin/python3
"""
This Python script takes in a URL, sends a request to it and displays
the value of the X-Request-Id variable, which is found in the header
of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
