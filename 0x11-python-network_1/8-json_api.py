#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""

if __name__ == "__main__"
    import sys
    import requests

    if sys.argv[1] is "":
        q = ""
    else:
        q = sys.argv[1]
    req = request.post('http://0.0.0.0:5000/search_user', q)
    results = req.json
    if results is None:
        print("No result")
    else:
        print("[{}] {}".format(results.id, results.name))
