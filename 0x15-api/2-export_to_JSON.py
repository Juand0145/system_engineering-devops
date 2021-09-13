#!/usr/bin/python3
"""Is Python script to export data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":

    USER_ID = argv[1]
    json_dict = {}

    request = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(argv[1])).json()

    USERNAME = request.get("username")

    request = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(argv[1])).json()

    json_dict[USER_ID] = [{"task": i.get("title"),
                           "completed": i.get("completed"),
                           "username": USERNAME} for i in request]

    with open(USER_ID + ".json", "w") as jsonfile:
        json.dump(json_dict, jsonfile)
