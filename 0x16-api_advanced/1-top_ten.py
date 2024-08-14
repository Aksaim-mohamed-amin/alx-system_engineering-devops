#!/usr/bin/python3
"""
Print top 10 posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """print top 10 posts for the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALX-APP'}
    params = {'limit': 10}

    rs = requests.get(url,
                      headers=headers,
                      params=params,
                      allow_redirects=False)

    if rs.status_code != 200:
        print('None')
    else:
        for post in rs.json()['data']['children']:
            print(post['data']['title'])
