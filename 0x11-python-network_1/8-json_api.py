#!/usr/bin/python3
"""
This Python script takes in a letter and sends a POST request to
a URL with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    res = requests.post(url, data={'q': q})

    try:
        res = res.json()

        if res:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except Exception:
        print('Not a valid JSON')
