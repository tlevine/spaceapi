import pytest

from .. import util

BREMEN = {
    'url': 'http://www.hackerspace-bremen.de',
    'lastchange': 1432128156,
    'api': '0.12',
    'lon': 8.805830955505371,
    'space': 'Hackerspace Bremen e.V.',
    'lat': 53.08177947998047,
    'address': 'Bornstraße 14/15, 28195 Bremen, Germany',
    'RESULT': {'ST3': 'OPEN', 'ST2': '1432128156726'},
    'logo': 'http://hackerspacehb.appspot.com/images/hackerspace_icon.png',
    'contact': {'phone': '+49 421 14 62 92 15',
    'twitter': '@hspacehb',
    'email': 'info@hackerspace-bremen.de'},
    'icon': {'open': 'http://hackerspacehb.appspot.com/images/status_auf_48px.png',
    'closed': 'http://hackerspacehb.appspot.com/images/status_zu_48px.png'},
    'SUCCESS': 'Status found',
    'open': True,
    'status': ''
}

@pytest.mark.parametrize('data, open', [(BREMEN, True)])
def test_parse(data, open):
    observed = util.open(data)
    assert observed == open
