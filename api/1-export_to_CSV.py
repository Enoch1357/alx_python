#! /usr/bin/python3
"""
This module export specific data in the CSV format.
"""
#! /usr/bin/python3
"""
This script accesses data from an API 'REST API',
for a given employee ID, then returns information
about his/her todo list progress.
"""
import sys
import requests
import csv
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
    completed_tasks = sum(1 for task in tasks if task["completed"])

    csvfileName = f"{employee_id}.csv"
    with open(csvfileName, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
    for task in tasks:
        writer.writerow([employee_id, employee_data['name'], task['completed'], task['title']])

if len(sys.argv) != 2:
    print("Usage error: python <script> <employee-id>")
else:
    employee_id = sys.argv[1]
    getTodoInfo(employee_id)
