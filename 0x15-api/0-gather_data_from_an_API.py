#!/usr/bin/python3
"""
returns information about a user TODO list progress, based on his id.
"""

import requests
import sys


if len(sys.argv) != 2:
    print(f"Usage {sys.argv[0]} <User ID>")
    exit
else:
    employeeID = sys.argv[1]

# Retrive the usrs name
rs = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employeeID}"
)
if rs.status_code != 200:
    print(
        f"Error retrieving the employee name {rs.status_code}: {rs.reason}"
    )
    exit
else:
    employeeName = rs.json()['name']

# Retrive the user tasks list
rs = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employeeID}/todos"
)
if rs.status_code != 200:
    print(f"Error retrieving user tasks list {rs.status_code}: {rs.reason}")
    exit
else:
    tasksList = rs.json()
    completedTasks = [task for task in tasksList if task['completed']]

print("Employee {} is done with tasks({}/{}):"
      .format(employeeName, len(completedTasks), len(tasksList)))
for task in completedTasks:
    print('\t', task['title'])
