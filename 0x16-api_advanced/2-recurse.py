#!/usr/bin/python3
"""this function queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing all titles
    of all hot articles for a given subreddit"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.recurse:v1.0 (by /u/username)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after')

        for child in children:
            hot_list.append(child.get('data', {}).get('title'))

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except requests.RequestException:
        return None
