#!/usr/bin/env python3
import os

from bottle import Bottle, request, response, \
                   abort, redirect, \
                   view, TEMPLATE_PATH, \
                   static_file

TEMPLATE_PATH.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))

app = Bottle()

@app.route('/')
@view('plot')
def home():
    return {
        'weeks': [
            {
                'date': '2015-07-01',
                'observations': [{'open': 'open', 'mirror_href': '.'} for _ in range(72)],
            },
        ] * 3,
        'hours': range(7, 7 + 6),
    }
