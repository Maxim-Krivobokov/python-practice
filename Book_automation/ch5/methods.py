# 3 methods for vocabilaries

# keys() , values(), items()

# they return types: dict_keys, dict_values, dict_items.
# these types are not lists, but can be used in "for" cycles
# dict_items is list of tuples (key1, value1); (key2, value2),...


book1 = {'name': 'LotR', 'Author': 'J.R.R.T.', 'pages': 1300, 'year': 1952}

book2 = {'name': 'haryPoter', 'author': 'Rowling', 'number': 7, 'year': '1997'}


for v in book1.values():
    print(v)

for k in book1.keys():
    print(k)


for i in book2.items():
    print(i)


# to get a real list we can use function list()

print(list(book1.keys()))

# group assignment for items()
for k, v in book1.items():
    print('Key is: ' + k + ' Value is: ' + str(v))

