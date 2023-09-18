#! /usr/bin/python3
"""
This module fetches the url 'https://alu-intranet.hbtn.io/status'.
"""
import requests
request = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(request.text)))
print("\t- content: {}".format(request.text))