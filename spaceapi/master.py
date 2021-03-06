import shelve, os

from . import download, util

def directory(minute = None):
    '''
    Maintain a master directory in case the Space API directory breaks.
    '''
    fn = os.path.join(download.DIR, 'master-directory')
    exists = (os.path.exists(fn + '.db') or os.path.exists(fn))

    with shelve.open(fn) as db:
        if not exists:
            rebuild_directory(db)
        if minute:
            update_directory(db, minute)
        data = dict(db)

    return data

def update_directory(db, minute):
    response = download.directory(minute)
    db.update(util.eat(response))

def rebuild_directory(db):
    for minute, response in download.directory.items():
        db.update(util.eat(response))
