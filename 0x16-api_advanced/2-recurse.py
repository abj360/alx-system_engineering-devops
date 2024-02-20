#!/usr/bin/python3
"""
This module returns list of titles of hot articles
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
        Recursive function to query Reddit API for given subreddit

        Returns a list of titles of all hot articles,
        or None if invalid subreddit
    """
    if type(subreddit) is list:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    r = r.json()
    if 'data' in r:
        data = r.get('data')
        if not data.get('children'):
            return hot_list
        hot_list += [post.get('data').get('title')
                     for post in data.get('children')]
        if not data.get('after'):
            return hot_list
        subreddit[1] = data.get('after')
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return hot_list
    else:
        return None
