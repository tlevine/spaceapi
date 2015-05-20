def eat(response):
    try:
        data = response.json()
    except ValueError:
        data = {}
