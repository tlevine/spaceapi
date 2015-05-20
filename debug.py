import datetime, csv, sys

import spaceapi

w = csv.writer(sys.stdout)
w.writerow(('datetime', 'hackerspaces'))
for k in sorted(spaceapi.download.directory.keys()):
    d = datetime.datetime.fromtimestamp(k).isoformat()
    try:
        v = spaceapi.download.directory[k].json()
    except ValueError:
        v = {}
    w.writerow((d, len(v)))
