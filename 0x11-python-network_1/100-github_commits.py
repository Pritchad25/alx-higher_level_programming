#!/usr/bin/python3
"""
This Python script takes 2 arguments list 10 commits
(from the most recent to oldest) of the repository “rails” by
the user “rails”.
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            owner, repo)
    param = {'per_page': 10}

    res = requests.get(url, params=param)

    if res.status_code == 200:
        data = res.json()

        for commit in data:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')

            print("{}: {}".format(sha, author))
