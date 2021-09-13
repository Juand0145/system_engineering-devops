#!/usr/bin/python3
"""Is a Python script to export data in the CSV format"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    USER_ID = argv[1]
    request = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(USER_ID)).json()
    USERNAME = request.get("username")
    request = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(USER_ID)).json()

    with open(USER_ID + ".csv", "w") as csv_file:
        file = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for i in request:
            file.writerow(
                [argv[1], USERNAME, i.get("completed"), i.get("title")])
