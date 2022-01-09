#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
Please test your script in the container provided,
using the web server running on port 5000
"""
import urllib.request
import sys


if __name__ == "__main__":
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print("{}".format(response.read().decode('utf-8')))
