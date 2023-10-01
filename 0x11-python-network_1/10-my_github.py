#!/usr/bin/python3
"""
This Python script takes my GitHub credentials (username and password)
and uses the GitHub API to display my id.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    res = requests.get(url, auth=(username, password))

    if res.status_code == 200:
        user = res.json()
        print(user.get('id'))
    else:
        print("None")
