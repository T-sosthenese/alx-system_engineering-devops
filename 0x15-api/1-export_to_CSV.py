#!/usr/bin/python3
"""
Exporting employee todo data using CSV format
"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as f:
        for task in tasks:
            f.write('"{}", "{}", "{}", "{}"\n'
                    .format(employeeId, username, task.get('completed'),
                            task.get('title')))
