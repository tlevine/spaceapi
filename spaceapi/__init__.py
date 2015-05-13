import datetime, sys, csv
from concurrent.futures import ThreadPoolExecutor

from . import download

def main():
    # Download
    timestamp = int(datetime.datetime.now().timestamp())
    minute = timestamp - (timestamp % (5 * 60))
    with ThreadPoolExecutor(30) as e:
        for space in download.directory(minute).json().values():
            e.submit(download.space, (minute, space))

    # Emit
    for minute in download.directory.keys():
        for space in download.directory[minute].json().values():
            open = download.space[minute, space].get('state', {}).get('open')
            print(open)

main()
