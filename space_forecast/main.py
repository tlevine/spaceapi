#!/usr/bin/env python3
import os, datetime

from bottle import Bottle, request, response, \
                   abort, redirect, \
                   view, TEMPLATE_PATH, \
                   static_file

from .util import earlier_later

TEMPLATE_PATH.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))

app = Bottle()

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
HOURS = list(range(24))
SPACES = {'Hackistan'}

@app.route('/')
@view('home')
def home():
    return {'spaces': sorted(SPACES)}

@app.route('/<space>')
@view('plot')
def plot_space(space):
    n = datetime.datetime.now()
    day = n.strftime('%A')
    hour = n.hour
    return plot_hour(space, day, hour)

@app.route('/<space>/<day>')
@view('plot')
def plot_day(space, day):
    redirect('/%s/%s/12' % (space, day))

@app.route('/<space>/<day>/<hour:int>')
@view('plot')
def plot_hour(space, day, hour):
    if space not in SPACES:
        abort(404, 'Bad space')
    elif day not in DAYS:
        abort(404, 'Bad day')
    elif hour not in HOURS:
        abort(404, 'Bad hour')

    radius = 2
    hours = list('%02d:00' % (h % 24) for h in range(hour - radius, hour + radius + 1))

    data = {
        'space': space,
        'weeks': [
            {
                'date': '2015-07-01',
                'observations': [{'open': 'open', 'mirror_href': '.'} for _ in range(60)],
            },
        ] * 3,
        'hours': hours,
    }
    data.update(earlier_later(day, hour, radius))
    return data


@app.route('/raw/<space>/<year:int>/<month:int>/<day:int>/<hour:int>/<minute:int>')
@view('raw')
def raw(space, year, month, day, hour, minute):
    d = datetime.datetime(year, month, day, hour, minute)
    return {
        'space': space,
        'date': d.strftime('%Y-%m-%d %H:%M UTC'),
        'body': 'blah blah',
    }
