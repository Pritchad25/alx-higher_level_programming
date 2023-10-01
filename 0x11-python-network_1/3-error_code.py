#!/usr/bin/python3
"""This Python script takes in a URL, sends a request to it
and displays the body of the response."""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
