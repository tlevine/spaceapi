import os

import requests, vlermv

DIR = os.path.expanduser('~/.spaceapi')
HEADERS = {
    'User-Agent': 'https://pypi.python.org/pypi/spaceapi',
}

@vlermv.cache(DIR, 'directory', mutable = False)
def directory(datetime):
    url = 'http://spaceapi.net/directory.json'
    return requests.get(url, headers = HEADERS)

@vlermv.cache(DIR, 'space', mutable = False)
def space(datetime, url):
    return requests.get(url, verify = False, headers = HEADERS)
