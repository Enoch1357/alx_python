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
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    request = requests.get(todos_url)
    tasks = request.json()
    total_tasks = 0
    completed_tasks = 0
    for i in tasks:
        if i['userId'] == employee_id:
            total_tasks += 1
        if (i['completed'] and i['userId'] == employee_id):
            completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(employee_data.get('name'), completed_tasks, tasks))
    for task in tasks:
        if task.get('completed') == True:
            print(f"\t {task.get('title')}")

if len(sys.argv) != 2:
    print("Usage error: python <script> <employee-id>")
else:
    employee_id = int(sys.argv[1])
    getTodoInfo(employee_id)
