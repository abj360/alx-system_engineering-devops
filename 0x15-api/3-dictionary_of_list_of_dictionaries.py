#!/usr/bin/python3
"""
This module returns information about all employees TODO list
and saves it to json
"""
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"

    employees = requests.get(url).json()

    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # save to json
    data = {}
    with open("todo_all_employees.json".format(id), "w") as f:
        for employee in employees:
            id = employee.get("id")
            task_list = []
            for task in tasks:
                if task.get("userId") == id:
                    user = {}
                    user["task"] = task.get("title")
                    user["completed"] = task.get("completed")
                    user["username"] = employee.get("username")
                    task_list.append(user)
            user_info = {"{}".format(id): task_list}
            data.update(user_info)
        f.write(json.dumps(data))
