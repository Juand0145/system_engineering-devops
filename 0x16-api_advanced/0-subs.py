#!/usr/bin/python3
""" How many subs? file"""
import requests


def number_of_subscribers(subreddit):
    """scrypt to search the number f suscriber in the reddit api"""
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-agent": "custom"})
    if(r.status_code == 200):
        return r.json().get("data").get("subscribers")
    return 0
