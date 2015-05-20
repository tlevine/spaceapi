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
    return open_str[data.get('state', {}).get('open')]
