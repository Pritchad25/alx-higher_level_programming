#!/usr/bin/python3
"""
This Python script takes in a URL and an email, sends a POST request
to the URL with the email as a parameter, and displays the body
of the response.
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = urllib.parse.urlencode(email).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        res = response.read()
        print(res.decode('utf-8'))
