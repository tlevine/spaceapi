import datetime, sys
from concurrent.futures import ThreadPoolExecutor

from . import download, master, util

def get(resolution = 5 * 60, threads = 30):
    # Download
    timestamp = int(datetime.datetime.now())
    minute = datetime.datetime.fromtimestamp(timestamp - (timestamp % (resolution)))
    with ThreadPoolExecutor(threads) as e:
        urls = master.directory(minute).values()
        futures = [(url, e.submit(download.space, minute, url)) for url in urls]
    for url, future in futures:
        if future.exception() is not None:
            sys.stderr.write('Exception downloading %s:\n%s\n\n' % (url, future.exception()))

def read():
    spaces = master.directory()
    for minute in download.directory.keys():
        for space, url in spaces.items():
            key = minute, url
            if key not in download.space:
               #sys.stderr.write('%s was not saved at %s\n' % (url, minute))
                continue

            response = download.space[key]
            if response.ok:
                data = util.eat(response)
                open = util.open(data)
            else:
                open = 'NA'
            yield space, minute, open

def emit():
    import csv
    w = csv.writer(sys.stdout)
    w.writerow(('space', 'timestamp', 'open'))
    w.writerows(read())

def main():
    import argparse
    p = argparse.ArgumentParser(description = 'Download Space API data.')
    p.add_argument('-d', '--download', help = 'Download new data?',
                   action = 'store_true')
    p.add_argument('-t', '--threads', default = 30, type = int,
                   help = 'Number of threads to use for downloading, default is 30')
    p.add_argument('-e', '--csv', help = 'Emit data as CSV?',
                   action = 'store_true')
    args = p.parse_args()

    if args.download:
        get(threads = args.threads)

    if args.csv:
        emit()

    if not args.download and not args.csv:
        sys.stderr.write('Doing nothing; try running with the --help flag.\n')
        sys.exit(1)
