#!/usr/bin/python3
"""
returns information about a user TODO list progress, based on his id.
end export the result to json file
"""

import json
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

    todos = []
    for task in tasksList:
        todos.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': userName
        })

    with open(f"{employeeID}.json", 'w') as file:
        json.dump({employeeID: todos}, file)
