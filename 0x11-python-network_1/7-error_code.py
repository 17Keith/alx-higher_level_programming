#!/usr/bin/python3
"""Takes a given URL and displays the response"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if __name__ == "__main__":
        res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
