#!/usr/bin/python3
""" How many subs? file"""
import requests


def top_ten(subreddit):
    """scrypt to search the number fo 10 hot spots"""
    r = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10".
                     format(subreddit), headers={"User-agent": "custom"})

    if(r.status_code == 200):
        for i in r.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print("None")
