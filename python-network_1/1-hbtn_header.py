#! /usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.
"""
import requests
import sys
url = sys.argv[1]
request = requests.get(url)
if 'X-Request-Id' in headers:
    print(request.headers['X-Request-Id'])
else:
    print(None)