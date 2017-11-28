#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable found
in the header of the response.
'''

import urllib.request
import sys
url_arg = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(url_arg) as response:
    display = response.getheader('X-Request-Id')
    print(display)
