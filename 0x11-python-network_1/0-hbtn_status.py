#!/usr/bin/python3
'''
python script that fetches https://intranet.hbtn.io/status
'''

import urllib.request
req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    display = response.read()
    print("Body response:")
    print("\t- type:", type(display))
    print("\t- content:", display)
    print("\t- utf8 content:", display.decode('utf8'))
