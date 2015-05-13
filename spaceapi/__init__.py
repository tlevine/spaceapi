import datetime, sys, csv

from . import download


def main():
    # Download
    timestamp = int(datetime.datetime.now().timestamp())
    for space in download.directory(timestamp).values():
        download.space(timestamp, space)

    # Emit
    for timestamp in map(int, download.directory.keys()):
        for space in download.directory[timestamp].values():
            open = download.space[timestamp, space].get('state', {}).get('open')
            print(open)

main()
