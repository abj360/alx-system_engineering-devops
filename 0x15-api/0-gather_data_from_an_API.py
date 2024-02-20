#!/usr/bin/python3
"""
This module returns information about an employee's TODO list progress
"""
import requests
from sys import argv

if __name__ == '__main__':
    # Get employee id from arguments
    id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    employee = requests.get(url).json()
    employee_name = employee.get("name")

    done = 0
    total = 0
    done_tasks = []
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    for task in tasks:
        if task.get("userId") == id:
            total += 1
            if task.get("completed") is True:
                done_tasks.append(task.get("title"))
                done += 1
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, total
    ))
    for task in done_tasks:
        print("\t {}".format(task))
