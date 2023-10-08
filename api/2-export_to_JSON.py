#! /usr/bin/python3.4.3
"""
This script accesses data from an API 'REST API',
for a given employee ID, then returns information
about his/her todo list progress.
The exports the info into a csv file.
"""
import json
import requests
import sys
__name__ = '__main__'

class MyEncoder(json.JSONEncoder):
    def encode(self, obj):
        def json_encode_string(s):
            return f'"{s}"'

        def json_encode_dict(d):
            pairs = [f'"{key}": {json_encode(val)}' for key, val in d.items()]
            return "{" + ", ".join(pairs) + "}"

        def json_encode(val):
            if isinstance(val, str):
                return json_encode_string(val)
            elif isinstance(val, dict):
                return json_encode_dict(val)
            else:
                return json.JSONEncoder().encode(val)

        return json_encode(obj)

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
    todo_data = {
        employee_id: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": name
            }
            for task in todos
        ]
    }
    
    #Creating a JSON file
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as jsonfile:
        json.dump(todo_data, jsonfile, cls=MyEncoder)

if len(sys.argv) != 2:
    print("Usage error: python <script> <employee-id>")
else:
    employee_id = int(sys.argv[1])
    getTodoInfo(employee_id)
