# using vocabilary with another vocabilary
allGuests = {'Alice': {'apples': 5, 'pepsi': 2},
             'Bob': {'sandwitches': 7, 'apples': 2},
             'Carol': {'beer': 5, 'vodka': 7},
             'Akaki': {'wine': 25, 'beer': 3}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought:')
print(' - apples       ' + str(totalBrought(allGuests, 'apples')))
print(' - pepsi        ' + str(totalBrought(allGuests, 'pepsi')))
print(' - sandwitches  ' + str(totalBrought(allGuests, 'sandwitches')))
print(' - beer         ' + str(totalBrought(allGuests, 'beer')))
print(' - vodka        ' + str(totalBrought(allGuests, 'vodka')))
print(' - wine        ' + str(totalBrought(allGuests, 'wine')))
print(' - condoms      ' + str(totalBrought(allGuests, 'condoms')))
