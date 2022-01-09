#!/usr/bin/python3
from urllib import request
"""
Python script that fetches https://intranet.hbtn.io/status
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed
like the following example (tabulation before -)
You must use a with statement
"""

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as f:
        response = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
