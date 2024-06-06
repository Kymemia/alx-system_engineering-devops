#!/usr/bin/python3
"""this function queries the Reddit API and prints
the titles of the first 10 hot posts
listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """returns titles of first 10 hot posts listed
    for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agnt": "python:subreddit.top.ten:v1.0 (by /u/username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for x, post in enumerate(posts[:10]):
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
