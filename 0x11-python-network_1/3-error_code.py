#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print("{}".format(response.read().decode('utf-8')))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.read().decode("utf8")))
