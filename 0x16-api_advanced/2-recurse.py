#!/usr/bin/python3
""" How many subs? file"""


def recurse(subreddit, hot_list=[], counter = 0):
    """scrypt to search the number fo 10 hot spots"""
    import requests
    import json

    auth = requests.auth.HTTPBasicAuth(
        'm8o3DcygIBR6fKDWjyNaUA', 'VMkfMswZ-UlQqUjyxYC-ZRPCq45q-g')

    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password',
            'username': 'Juand01445',
            'password': 'Dolex0145'}

    # setup our header info, which gives reddit a brief description of our app
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    try:
        url = 'https://oauth.reddit.com/r/{:s}/hot'.format(subreddit)
        byte_string = requests.get(
            url, headers=headers, params={"limit": 100000000}).content
        decoded_string = byte_string.decode("utf8")
        json_dictionary = json.loads(decoded_string)

        hot_spots = json_dictionary["data"]["children"]

        if (counter < len(hot_spots)):
            element = hot_spots[counter]
    
            hot_list.append(element["data"]["title"])
            counter += 1
            return recurse(subreddit, hot_list, counter)

        else:
            return (hot_list)

    except(KeyError):
        return (None)
