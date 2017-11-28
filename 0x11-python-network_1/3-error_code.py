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
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            decode_html = html.decode('utf8')
            print(decode_html)
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
