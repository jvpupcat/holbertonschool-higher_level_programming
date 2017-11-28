#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests

    try:
        value = sys.argv[1]
    except:
        value = ""
    req = requests.post('http://0.0.0.0:5000', data={'q': value})
    try:
        results = req.json()
        if not results:
            print("No result")
        else:
            print("[{}] {}".format(results.get('id'), results.get('name')))
    except ValueError:
        print("Not a valid JSON")
