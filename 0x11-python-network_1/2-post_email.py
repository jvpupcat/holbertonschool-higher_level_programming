#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
(decoded in utf-8)
'''

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    data = {}
    data['email'] = sys.argv[2]
    value = urllib.parse.urlencode(data)
    value = value.encode('ascii')

    req = urllib.request.Request(url, value)
    with urllib.request.urlopen(req) as response:
        read = response.read()
        decode = read.decode('utf8')
    print(decode)
