#!/usr/bin/env python3
import os, datetime

from bottle import Bottle, request, response, \
                   abort, redirect, \
                   view, TEMPLATE_PATH, \
                   static_file

TEMPLATE_PATH.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'views')))

app = Bottle()

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
HOURS = list(range(24))
SPACES = {'Hackistan'}

@app.route('/<space>')
@view('plot')
def plot_space(space):
    redirect('/' + space + datetime.datetime.now().strftime('/%A/%H'))

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

def earlier_later(day, hour, radius):
    ed, eh = clock_time(day, hour - radius)
    ld, lh = clock_time(day, hour + radius)
    return {
        'earlier_day': ed,
        'earlier_hour': eh,
        'later_day': ld,
        'later_hour': lh,
    }

def clock_time(day, hour):
    if 0 <= hour <= 23:
        return day, hour
    
    i = DAYS.index(day)
    if i == 0:
        i = i + len(DAYS)

    if hour < 0:
        return DAYS[i - 1], hour + 24
    
    if hour > 23:
        return DAYS[i + 1], hour - 24
