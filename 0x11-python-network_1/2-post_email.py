#!/usr/bin/python3
"""Takes a given URL and email and sends a POST request to the URL"""

if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
