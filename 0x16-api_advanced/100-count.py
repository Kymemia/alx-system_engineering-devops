#!/usr/bin/python3
"""this function queries the Reddit API,
parses the title of all hot articles,
& prints a sorted count of given keywords
(case-sensitive, delimited by spaces) by spaces"""

import re
import requests


def count_words(subreddit, word_list, word_count=None, after_token=None):
    """returns a sorted count of given keywords
    """
    if word_count is None:
        word_count = {}

    if after_token is None:
        after_token = ""

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-Agent": "python:subreddit.wordcount:v1.0 (by /u/username)"
            }

    response = requests.get(
            base_url,
            params={"after": after_token},
            headers=headers,
            allow_redirects=False
            )

    if response.status_code != 200:
        return None

    after_token = response.json().get("data", {}).get("after")
    for post in response.json().get("data", {}).get("children", []):
        title = post.get('data', {}).get('title', '').lower()

        for word in word_list:
            word_lower = word.lower()
            pattern = r'\b{}\b'.format(re.escape(word_lower))
            matches = re.findall(pattern, title)

            word_count[word_lower] = (
                    word_count.get(word_lower, 0) + len(matches)
            )

    for word in word_list:
        if word.lower() not in word_count:
            word_count[word.lower()] = 0

    if after_token:
        return count_words(subreddit, word_list, word_count, after_token)

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        if count > 0:
            print(f'{word}: {count}')

    return word_count
