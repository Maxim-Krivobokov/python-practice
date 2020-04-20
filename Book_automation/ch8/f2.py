import shelve

storage = shelve.open('data1')
storage['cats'] = 'barsik mursik matroskin'

storage.close()

print('Hello')
