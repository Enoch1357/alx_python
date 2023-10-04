#! /usr/bin/python3
"""
This module takes in a letter and sends a POST request to 'http://0.0.0.0:5000/search_user' with the letter as a parameter.
"""
import sys
import requests
if len(sys.argv) < 2:
    q = ""
else:
    q = sys.argv[1]

try:
    request = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    request.raise_for_status()

    try:
        json_response = request.json()

        if json_response:
            print("[{}] {}".format(json_response.get("id"), json_response.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print("Not a valid JSON")
