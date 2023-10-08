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
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_count = 0
    todos_done = 0

    resp = requests.get(todos_url).json()
    for i in resp:
        if i['userId'] == id:
            todos_count += 1
        if (i['completed'] and i['userId'] == id):
            todos_done += 1

    resp = requests.get(users_url).json()

    name = None
    for i in resp:
        if i['id'] == id:
            name = i['name']
    todos = "https://jsonplaceholder.typicode.com/{}/todos".format(employee_id)
    for task in todos:
        if task.get('completed') == True:
            print(f"\t {task.get('title')}")

if len(sys.argv) != 2:
    print("Usage error: python <script> <employee-id>")
else:
    employee_id = int(sys.argv[1])
    getTodoInfo(employee_id)
