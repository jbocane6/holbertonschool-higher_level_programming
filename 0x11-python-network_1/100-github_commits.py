#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
    r = requests.get(url)
    r = r.json()
    for i in range(10):
        author = r[i].get('commit').get('author').get('name')
        sha = r[i].get('sha')
        print("{}: {}".format(sha, author))
