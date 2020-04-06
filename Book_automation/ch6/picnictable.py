def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwitches': 4, 'apples': 5, 'beer': 3, 'cookies': 9000}

printPicnic(picnicItems, 12, 5)

printPicnic(picnicItems, 20, 6)