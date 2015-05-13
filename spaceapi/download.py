import requests, vlermv

DIR = '~/.spaceapi'

@vlermv.cache(DIR, 'directory')
def directory(datetime):
    url = 'http://spaceapi.net/directory.json'
    return requests.get(url)

@vlermv.cache(DIR, 'space')
def space(datetime, url):
    return requests.get(url)
