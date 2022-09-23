#!/usr/bin/python3
"""Takes a given URL and email and sends a POST request to the URL"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
