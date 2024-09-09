#!/usr/bin/python3
"""
returns information about a user TODO list progress, based on his id.
end export the result to csv file
"""

import csv
import requests
import sys


def get_username(id):
    """Retrive the employee name"""
    rs = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    if rs.status_code != 200:
        print(f"Error retrieving employee name {rs.status_code}: {rs.reason}")
        return
    else:
        return rs.json()['username']


def get_tasks_list(id):
    # Retrive the user tasks list
    rs = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}/todos")
    if rs.status_code != 200:
        print(f"Error retrieving tasks list {rs.status_code}: {rs.reason}")
        return
    else:
        return rs.json()


if len(sys.argv) != 2:
    print(f"Usage {sys.argv[0]} <User ID>")
    exit
else:
    employeeID = sys.argv[1]
    userName = get_username(employeeID)
    tasksList = get_tasks_list(employeeID)

    with open(f"{employeeID}.csv", 'w') as file:
        for task in tasksList:
            row = [employeeID, userName, task['completed'], task['title']]
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(row)
