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

ONE_WEEK = 7 * 24 * 3600
def read(annotate = False, start = None):
    '''
    Read the data.
    
    :param bool annotate: Include extra information useful for plotting.
    :param datetime start: Read only the readings from a particular date on.
    '''
    spaces = master.directory()
    for minute in download.directory.keys():
        if start and minute < start:
            continue

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
                data = None
                open = 'NA'
            
            row = space, minute, open

            if annotate:
                week = int(minute.strftime('%W'))
                week_remainder = minute.timestamp() % week

                row += (week, week_remainder, data)

            yield row

def space_forecast_importer():
    start = datetime.datetime(2015, 2, 8) # Read this from a database.
    reader = read(annotate = True, start = start)

    with shelve.open('/tmp/spaceapi') as db:
        for space, minute, open, week, week_remainder, data in reader:
            db[(space, week, week_remainder)] = data

    with shelve.open('/tmp/chartdata') as db:
        for space, minute, open, week, week_remainder, data in reader:
            db[(space, week, week_remainder)] = open

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
