#!/usr/bin/env python3
import os

from bottle import Bottle, request, response, \
                   abort, redirect, \
                   view, TEMPLATE_PATH, \
                   static_file

TEMPLATE_PATH.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))

app = Bottle()

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
HOURS = list(range(24))
SPACES = {'Hackistan'}

@app.route('/<space>/<day>/<hour:int>')
@view('plot')
def home(space, day, hour):
    if space not in SPACES:
        abort(404, 'Bad space')
    elif day not in DAYS:
        abort(404, 'Bad day')
    elif hour not in HOURS:
        abort(404, 'Bad hour')

    radius = 2
    hours = range(hour - radius, hour + radius + 1)

    return {
        'space': space,
        'weeks': [
            {
                'date': '2015-07-01',
                'observations': [{'open': 'open', 'mirror_href': '.'} for _ in range(60)],
            },
        ] * 3,
        'hours': hours,
    }
