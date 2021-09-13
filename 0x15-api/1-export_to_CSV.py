#!/usr/bin/python3
"""Is a Python script to export data in the CSV format"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    USER_ID = argv[1]
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(USER_ID)).json()
    USERNAME = r.get("username")
    r = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                     format(USER_ID)).json()

    with open(USER_ID + ".csv", "w") as csvfile:
        f = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in r:
            f.writerow([argv[1], USERNAME, i.get("completed"), i.get("title")])
