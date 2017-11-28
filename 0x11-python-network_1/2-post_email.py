#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
(decoded in utf-8)
'''

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    email = {'Your email is': sys.argv[2]}
    display = urllib.request.urlopen(url, data=json.dumps(email))
    print(display)
