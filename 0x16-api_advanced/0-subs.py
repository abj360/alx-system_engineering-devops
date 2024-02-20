#!/usr/bin/python3
"""
This module queries the reddit API for the number of
subscribers to a particular subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Sends a query to reddit api for the number of subscribers
    """
    api_url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {
        "User-Agent": "CustomClient/1.0",
    }

    about = requests.get(api_url, headers=headers, allow_redirects=False)
    if about.status_code != 200:
        return 0
    elif "subscribers" in about.json().get("data"):
        return about.json().get("data").get("subscribers")
    return 0
