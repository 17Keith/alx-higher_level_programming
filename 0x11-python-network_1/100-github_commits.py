#!/usr/bin/python3
"""Prints a list of the first 10 commits from recent to oldest"""

if __name__ == "__main__":
    import requests
    from sys import argv

    reponame = argv[1]
    ownername = argv[2]

    r = requests.get(
        'https://api.github.com/repos/{}/{}/commits'
        .format(reponame, ownername))
    if r.status_code >= 400:
        print('None')
    else:
        for i in r.json()[:10]:
            print("{}: {}".format(i.get('sha'),
                                  i.get('commit').get('author').get('name')))
