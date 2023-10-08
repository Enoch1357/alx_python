#! /usr/bin/python3.4.3
"""
This script accesses data from an API 'REST API',
for a given employee ID, then returns information
about his/her todo list progress.
"""
import csv
import requests
import sys
__name__ = '__main__'
def getTodoInfo(employee_id):
    """
    This function takes in an integer parameter and 
    returns info of the employee that corresponds to the
    parameter given 'employee_id'
    """
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    todos_done = 0

    resp = requests.get(todos_url).json()
    todos_count = len(resp)
    for i in resp:
        if (i.get('completed')):
            todos_done += 1

    resp = requests.get(users_url).json()
    name = resp.get('username')

    employee_todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    todos = requests.get(employee_todo_url).json()

    # Create a CSV file
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": name,
                "TASK_COMPLETED_STATUS": task['completed'],
                "TASK_TITLE": task['title']
            })


if len(sys.argv) != 2:
    print("Usage error: python <script> <employee-id>")
else:
    employee_id = int(sys.argv[1])
    getTodoInfo(employee_id)
