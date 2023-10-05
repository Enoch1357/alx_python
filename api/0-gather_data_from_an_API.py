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
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.get('completed') == True)
    print(f"Employee {employee_data.get('name')} is done with tasks({completed_tasks}/{tasks}):")
    for task in tasks:
        if task.get('completed') == True:
            print(f"\t {task.get('title')}")

if len(sys.argv) != 2:
    print("Usage error: python <script> <employee-id>")
else:
    employee_id = int(sys.argv[1])
    getTodoInfo(employee_id)
