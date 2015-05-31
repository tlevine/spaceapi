def eat(response):
    try:
        data = response.json()
    except ValueError:
        data = {}
    return data

open_str = {
    True: 'TRUE',
    'true': 'TRUE',
    False: 'FALSE',
    'false': 'FALSE',
    None: 'NA',
}
def open(data):
    if 'open' in data:
        raw = data['open']
    else:
        try:
            raw = data.get('state', {}).get('open')
        except AttributeError:
            raw = None
    return open_str[raw]
