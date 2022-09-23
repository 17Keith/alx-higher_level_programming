#!/usr/bin/python3
"""Takes github cresentials and uses github api to display id"""

if __name__ == "__main__":
    import requests
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/user'
    request = requests.get(url, auth=(user, passwd))
    print(request.json().get('id'))
