#!/usr/bin/python3
"""Takes a request from a given URL and displays value of 'X-Request-Id'"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
