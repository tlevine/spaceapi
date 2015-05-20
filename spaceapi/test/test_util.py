import json

import pytest

from .. import util


ENTROPIA = json.loads('''{
    "api": "0.13",
    "contact": {
        "email": "info@entropia.de",
        "irc": "irc://irc.hackint.eu/#entropia",
        "issue_mail": "Zmxvcm9sZkBlbnRyb3BpYS5kZQ==",
        "ml": "news@entropia.de",
        "phone": "+49 721 5604732"},
    "icon": {
        "closed": "https://entropia.de/wiki/images/7/76/Clubstatus_zu.png",
        "open": "https://entropia.de/wiki/images/7/7a/Clubstatus_offen.png"},
    "issue_report_channels": [
        "issue_mail",
        "email"],
    "location": {
        "address": "Entropia e.V., Gewerbehof, Steinstraße 23, 76133 Karlsruhe, Germany",
        "lat": 49.0067,
        "lon": 8.407438 },
    "logo": "https://entropia.de/wiki/images/e/ed/Teebeutel1_noev.png",
    "open": true,
    "space": "Entropia",
    "state": {
        "icon": {
            "closed": "https://entropia.de/wiki/images/7/76/Clubstatus_zu.png",
            "open": "https://entropia.de/wiki/images/7/7a/Clubstatus_offen.png"
        },
        "lastchange": 1432126795,
        "open": true
    },
    "url": "https://entropia.de/"
}''')

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

testcases = [
    (BREMEN, 'TRUE'),
    (ENTROPIA, 'TRUE'),
]
@pytest.mark.parametrize('data, open', testcases)
def test_parse(data, open):
    observed = util.open(data)
    assert observed == open
