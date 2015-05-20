import shelve, os

from . import download

def directory(minute):
    '''
    Maintain a master directory in case the Space API directory breaks.
    '''
    fn = os.path.join(download.DIR, 'master-directory')
    if not (os.path.exists(fn + '.db') or os.path.exists(fn)):
        rebuild_directory(fn)
    update_directory(fn, minute)

def update_directory(fn, minute):
    with shelve.open(fn) as db:
        response = download.directory(minute)
        if len(response.text) > 0:
            db.update(response.json())

def rebuild_directory(fn):
    with shelve.open(fn) as db:
        for minute, response in download.directory.items():
            if len(response.text) > 0:
                spaces = response.json()
                db.update(spaces)
