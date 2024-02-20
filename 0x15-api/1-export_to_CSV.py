#!/usr/bin/python3
"""
This module returns information about an employee's TODO list
and saves it to csv
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    # Get employee id from arguments
    id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    employee = requests.get(url).json()
    employee_name = employee.get("username")

    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # save to csv
    attrs = ["userId", "username", "completed", "title"]
    with open("{}.csv".format(id), "w") as f:
        employee_writer = csv.DictWriter(
            f, fieldnames=attrs, quoting=csv.QUOTE_ALL)
        for task in tasks:
            if task.get("userId") == id:
                task["username"] = employee_name
                del task['id']
                employee_writer.writerow(task)
