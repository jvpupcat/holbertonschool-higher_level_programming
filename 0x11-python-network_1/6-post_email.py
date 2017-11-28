#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
(decoded in utf-8)
'''

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = {}
    email['email'] = sys.argv[2]
    req = requests.post(url, email)
    decode = req.decode("utf-8")
    print(decode)
