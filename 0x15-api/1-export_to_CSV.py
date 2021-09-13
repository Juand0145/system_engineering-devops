#!/usr/bin/python3
"""Is a Python script to export data in the CSV format"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    USER_ID = argv[1]

    request = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(argv[1])).json()

    USERNAME = request.get("name")

    request = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(argv[1])).json()

    with open("{}.csv".format(USER_ID), "w") as csv_file:
        file = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for i in request:
            file.writerow(
                [argv[1], USERNAME, i.get('completed'), i.get('title')])
