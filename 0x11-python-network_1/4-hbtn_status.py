#!/usr/bin/python3
'''
python script that fetches https://intranet.hbtn.io/status
'''

if __name__ == "__main__":
    import requests
    url = 'https://intranet.hbtn.io/status'
    req = requests.get(url)
    display = type(req.text)
    print("Body response:")
    print("\t- type:", display)
    print("\t- content:", req.text)
