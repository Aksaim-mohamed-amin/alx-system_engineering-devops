#!/usr/bin/python3
"""
returns information about a user TODO list progress, based on his id.
end export the result to json file
"""

import json
import requests
import sys


def get_tasks_list(id):
    # Retrive the user tasks list
    rs = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}/todos")
    if rs.status_code != 200:
        print(f"Error retrieving tasks list {rs.status_code}: {rs.reason}")
        return
    else:
        return rs.json()


rs = requests.get('https://jsonplaceholder.typicode.com/users')
if rs.status_code != 200:
    print(f"Error retrieving the users list {rs.status_code}: {rs.reason}")
    exit()
else:
    usersList = rs.json()

usersDict = {}
for user in usersList:
    userID = user['id']
    todos = get_tasks_list(userID)

    tasksList = []
    for task in todos:
        tasksList.append({
            'username': user['username'],
            'task': task['title'],
            'completed': task['completed']
        })

    usersDict.update({userID: tasksList})

with open('todo_all_employees.json', 'w') as file:
    json.dump(usersDict, file)
