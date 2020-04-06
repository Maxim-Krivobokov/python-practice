# get() method - takes two arguments  - key and default value ( default if key is not presented)


cash = {'dollars': 500, 'rubles': '2000', 'euro': 200}
print('I have ' + str(cash.get('dollars', 0)) + ' of dollars')

print('I have ' + str(cash.get('swiss franks', 0)) +
      ' of CHF')  # that will show default value = 0


# setfefault() - takes two arguments - key and default value for it

cat = {'name': 'Barsik', 'age': '5 years', 'gender': 'kastrat'}
cat.setdefault('color', 'black')
print('vocabilary cat:')
print(cat)


# second calling of setdefault() will do nothing, because cat['color'] is already set
cat.setdefault('color', 'white')
print(cat)
print(cat['color'])
