#!/usr/bin/python3
"""Takes a given URL and displays the response"""

if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
