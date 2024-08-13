#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ALX-APP'}

    rs = requests.get(url, headers=headers, allow_redirects=False)
    if rs.status_code == 200:
        return rs.json()['data']['subscribers']
    else:
        return 0
