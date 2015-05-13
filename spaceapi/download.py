import requests, vlermv

DIR = '~/.spaceapi

@vlermv.cache()
def directory(datetime):
    url = 'http://spaceapi.net/directory.json'
    return requests.get(url)

@vlermv.cache(
