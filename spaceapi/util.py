def eat(response):
    try:
        data = response.json()
    except ValueError:
        data = {}
    return data

def open(data):
    return False
