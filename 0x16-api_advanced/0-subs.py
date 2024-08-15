#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import json
import requests
import sys

def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """
    user_name = 'ledbag123'
    pass_word = 'Reddit72'
    user_pass_dict = {'user': user_name, 'passwd': pass_word, 'api_type': 'json'}
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)
