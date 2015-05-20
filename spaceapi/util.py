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
        raw = data.get('state', {}).get('open')
    return open_str[raw]
