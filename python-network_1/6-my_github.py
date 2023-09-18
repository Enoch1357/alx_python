#! /usr/bin/python3
"""
This module takes your GitHub credentials (username and password) and uses the GitHub API to display your id.
"""
import sys
import requests
username = sys.argv[1]
password = sys.argv[2]

url = 'https://api.github.com/user'
auth = (username, password)

try:
    request = requests.get(url, auth=auth)
    response = request.json()

    # Display the user's ID
    print(response['id'])

except ValueError:
    print("Not a valid JSON response")

except KeyError:
    print(None)

