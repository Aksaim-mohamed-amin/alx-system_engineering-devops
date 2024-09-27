#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers to a subreddit or 0 if invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }


    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the response status is not 200, subreddit is invalid
        if response.status_code != 200:
            print(response.status_code, response.reason)
            return 0
        
        data = response.json()
        return data['data']['subscribers']
    
    except Exception:
        # In case of any error (invalid subreddit, etc.), return 0
        return 0
