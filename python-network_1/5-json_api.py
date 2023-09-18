#! /usr/bin/python3
"""
This module takes in a letter and sends a POST request to 'http://0.0.0.0:5000/search_user' with the letter as a parameter.
"""
import sys
import requests
if len(sys.argv) == 1:
    q = ""
elif len(sys.argv) == 2:
    q = sys.argv[1]
request = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
response = request.json()
user = response[0]
try:
    if user:
        print("[{}] {}".format(user['id'], user['name']))
    else:
        print('No result')

except ValueError:
        print("Not a valid JSON")