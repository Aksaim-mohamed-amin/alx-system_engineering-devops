#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    rs = requests.get(url)
    if rs.status_code == 200:
        return rs.json()['data']['subscribers']

    return 0
