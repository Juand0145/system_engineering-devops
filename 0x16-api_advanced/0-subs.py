#!/usr/bin/python3
""" How many subs? file"""


def number_of_subscribers(subreddit):
    """scrypt to search the number f suscriber in the reddit api"""
    import requests
    import json

    # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
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

    # while the token is valid (~2 hours) we just add headers=headers to our requests

    try:
        byte_string = requests.get(
            'https://oauth.reddit.com/r/{:s}/about.json'.format(subreddit), headers=headers).content
        decoded_string = byte_string.decode("utf8")
        json_dictionary = json.loads(str(decoded_string))

        return(json_dictionary["data"]["subscribers"])

    except:
        return (0)
