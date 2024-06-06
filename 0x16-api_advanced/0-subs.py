#!/usr/bin/python3
"""this function returns the number
of subcribers for a given subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """gives a total of the number
    of subcribers in a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User-Agent: subreddit subscriber count"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0

    except requests.RequestException:
        return 0
