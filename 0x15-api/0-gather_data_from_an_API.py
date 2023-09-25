#!/usr/bin/python3
"""
A script that displays the todo list progess of employees
based on the employee ID provided as an argument.
"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get("name")

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    finished = 0
    finished_tasks = []

    for task in tasks:
        if task.get('completed'):
            finished_tasks.append(task)
            finished += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, finished, len(tasks)))

    for task in finished_tasks:
        print("\t {}".format(task.get('title')))
