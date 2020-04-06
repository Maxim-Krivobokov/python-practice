spam = ['hello', 'hi', 'preved', 'salut', 'buenos dias']
print(spam.index('salut'))

print(spam.index('hi'))


pets = ['cat', 'dog', 'parrot']

pets.insert(1, 'lizard')  # adding  into index 1
pets.append('mouse')  # adding to the tail of list

# methods insert and append return None


# remove() is method for values
# list.remove('value')
# del() is instruction for indexes

# del list[index]

print(pets)
try:
    pets.remove('lizard')
except ValueError:
    print('wrong pet, not in list')

del pets[0]
print(pets)

animals = ['cow', 'buffalo', 'giraffe', 'Crocodile',
           'bear', 'antilope', 'Hypopotame', 'Zebra']
sort_numbers = [2, 5, 3.14, 1, 55, - 7]
ancients = ['Trylobites', 'composognatus', 'dyplodoc',
            'Tiranosuaurus', 'Endrusarx', 'godzilla']

sort_numbers.sort()  # this function returns None
# strings are sorted in ASCII order( A-> Z, a->z, a after Z). Reverse is for reverse order


animals.sort(reverse=True)
print(sort_numbers)
print(animals)
# sorting in alphabetical order, ignoring upper and lower case
ancients.sort(key=str.lower)
print(ancients)
