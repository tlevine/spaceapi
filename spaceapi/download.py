import requests, vlermv

DIR = '~/.spaceapi'
HEADERS = {
    'User-Agent': 'https://pypi.python.org/pypi/spaceapi',
}

class int_transformer:
    def to_path(timestamp):
        return ('%d' % timestamp,)
    def from_path(path):
        assert len(path) == 1, path
        return int(path[0])

@vlermv.cache(DIR, 'directory', key_transformer = int_transformer, mutable = False)
def directory(timestamp):
    url = 'http://spaceapi.net/directory.json'
    return requests.get(url, headers = HEADERS)

@vlermv.cache(DIR, 'space', mutable = False)
def space(datetime, url):
    return requests.get(url, verify = False, headers = HEADERS)
