import json
import requests
import sys

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

def getAllTodoInfo():
    """
    This function retrieves todo information for all employees and exports it in JSON format.
    """
    all_todo_data = {}

    # Get the list of all user IDs
    user_ids = [user['id'] for user in requests.get("https://jsonplaceholder.typicode.com/users").json()]

    for employee_id in user_ids:
        users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todos_done = 0

        resp = requests.get(todos_url).json()
        todos_count = len(resp)
        for i in resp:
            if (i.get('completed')):
                todos_done += 1

        resp = requests.get(users_url).json()
        name = resp.get('username')

        employee_todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todos = requests.get(employee_todo_url).json()
        todo_data = [{
            "username": name,
            "task": task['title'],
            "completed": task['completed']
        } for task in todos]
        
        all_todo_data[employee_id] = todo_data

    # Creating a JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump(all_todo_data, jsonfile, cls=MyEncoder)

if __name__ == '__main__':
    getAllTodoInfo()
