#!/usr/bin/python3
"""
This module export specific data in the CSV format.
"""
import csv
import requests
import sys
def getTodoInfo(employee_id):
    """
    This function takes in an integer parameter and 
    returns info of the employee that corresponds to the
    parameter given 'employee_id'
    """
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    resp = requests.get(employee_url).json()
    name = resp.get('name')
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    tasks = requests.get(todos_url).json()

    csvfileName = f"{employee_id}.csv"
    with open(csvfileName, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([employee_id, name, task.get('completed'), task.get('title')])

if len(sys.argv) != 2:
    print("Usage error: python <script> <employee-id>")
else:
    employee_id = int(sys.argv[1])
    getTodoInfo(employee_id)
