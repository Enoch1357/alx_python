#! /usr/bin/python3.4.3
"""
This script accesses data from an API 'REST API',
for a given employee ID, then returns information
about his/her todo list progress.
"""
import requests
import sys
def getTodoInfo(employee_id):
    """
    This function takes in an integer parameter and 
    returns info of the employee that corresponds to the
    parameter given 'employee_id'
    """
    users_url = f'https://jsonplaceholder.typicode.com/users/'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    todos_url = f'https://jsonplaceholder.typicode.com/users//todos'
    todos_count = 0
    todos_done = 0

    request = requests.get(todos_url).json()
    for i in request:
        if i['userId'] == employee_id:
            todos_count += 1
        if (i['completed'] and i['userId'] == employee_id):
            todos_done += 1

    request = requests.get(users_url).json()

    name = None
    for i in request:
        if i['id'] == employee_id:
            name = i['name']
    print("Employee {} is done with tasks({}/{}):".format(name, todos_done, todos_count))
    for task in tasks:
        if task.get('completed') == True:
            print(f"\t {task.get('title')}")

if len(sys.argv) != 2:
    print("Usage error: python <script> <employee-id>")
else:
    employee_id = int(sys.argv[1])
    getTodoInfo(employee_id)
