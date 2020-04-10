import shelve

import pprint

shfile = shelve.open('newdata')
cats = ['Musya', 'Barsik', 'Simon']

shfile['cats'] = cats

shfile.close

shfile2 = shelve.open('newdata')
print(type(shfile2))

print(shfile2['cats'])

print(list(shfile2.keys()))

print(list(shfile2.values()))

shfile2.close()

cars = [{'brand': 'BMW', 'model': 'M3', 'power': 343}, {'brand': 'Audi', 'model': 'Rs4', 'power': 380}]

fileObj = open('mycars.py', 'w')
fileObj.write('cars =' + pprint.pformat(cars) + '\n')
#pprint.pformat(cats)

fileObj.close()