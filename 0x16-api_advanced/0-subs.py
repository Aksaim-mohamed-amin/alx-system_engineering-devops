#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    """
    # Set up a custom User-Agent to avoid 429 Too Many Requests error
    headers = {"User-Agent": "CustomUserAgent/0.1 by aksaimamin"}

    # Make a GET request to the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and contains the needed data
    if response.status_code == 200:
        data = response.json().get('data')
        if data and 'subscribers' in data:
            return data.get('subscribers')
    return 0
