import shelve, os

from . import download

def directory(minute):
    '''
    Maintain a master directory in case the Space API directory breaks.
    '''
    fn = os.path.join(download.DIR, 'master-directory')
    if os.path.exists(fn):
        rebuild_directory(fn)
    update_directory(fn, minute)

def update_directory(fn, minute):
    with shelve.open(fn) as db:
        response = download.directory(minute)
        if len(response.text) > 0:
            db.update(response.json())

def rebuild_directory(fn):
    with shelve.open(fn) as db:
        for minute, spaces in download.directory.items():
            db.update(spaces)
