#!/usr/bin/python3
"""
This module returns information about an employee's TODO list
and saves it to json
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    # Get employee id from arguments
    id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    employee = requests.get(url).json()
    employee_name = employee.get("username")

    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # save to json
    task_list = []
    with open("{}.json".format(id), "w") as f:
        for task in tasks:
            if task.get("userId") == id:
                user = {}
                user["task"] = task.get("title")
                user["completed"] = task.get("completed")
                user["username"] = employee_name
                task_list.append(user)
        f.write(json.dumps({"{}".format(id): task_list}))
