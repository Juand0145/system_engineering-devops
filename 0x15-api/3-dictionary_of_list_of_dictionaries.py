#!/usr/bin/python3
"""Is Python script to export data in the JSON format"""
import json
import requests


if __name__ == "__main__":

    json_dict = {}

    request_1 = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    request_2 = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    json_dict = {j.get("id"): [{"task": i.get("title"),
                               "completed": i.get("completed"),
                                "username": j.get("username")}
                               for i in request_2
                               if i.get("userId") == j.get("id")]
                 for j in request_1}

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_dict, jsonfile)
