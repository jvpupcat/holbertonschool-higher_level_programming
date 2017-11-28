#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable found
in the header of the response.
"""

if __name__ == "__main__":
    import requests
    import sys
    url_arg = sys.argv[1]
    req = requests.get(url_arg)
    display = req.headers.get('X-Request-Id', '')
    print(display)
