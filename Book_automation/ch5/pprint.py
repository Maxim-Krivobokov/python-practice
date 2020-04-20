import pprint

cars = [{'brand': 'BMW', 'model': 'M3', 'power': 343},
        {'brand': 'Audi', 'model': 'RS4', 'power': 380}]

txt = pprint.pformat(cars)

print(txt)
