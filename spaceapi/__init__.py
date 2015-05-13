import datetime, sys, csv
from concurrent.futures import ThreadPoolExecutor

from . import download

def download_all():
    # Download
    timestamp = int(datetime.datetime.now().timestamp())
    minute = timestamp - (timestamp % (5 * 60))
    with ThreadPoolExecutor(30) as e:
        spaces = download.directory(minute).json().values()
        futures = [(space, e.submit(download.space, minute, space)) for space in spaces]
    for space, future in futures:
        if future.exception() is not None:
            sys.stderr.write('Exception downloading %s:\n%s\n\n' % (space, future.exception()))

def emit():
    w = csv.writer(sys.stdout)
    w.writerow(('space', 'timestamp', 'open'))
    for minute in download.directory.keys():
        for space, url in download.directory[minute].json().items():
            response = download.space[minute, url]
            if response.ok:
                open = response.json().get('state', {}).get('open')
            else:
                open = None
            open_str = {
                True: 'TRUE',
                False: 'FALSE',
                None: 'NA',
            }[open]
            w.writerow((space, minute, open))

def main():
    download()
    emit()
