#! /usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.
"""
import sys
import requests
def req_sender(url=""):
    request = requests.get(url)
    print(request.headers['X-Request-Id'])
