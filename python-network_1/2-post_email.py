#! /usr/bin/python3
"""
This module takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""
import sys
import requests
url = sys.argv[1]
email = sys.argv[2]
request = requests.post(url, data={'email': email})
print("Your email is: {}".format(email))
