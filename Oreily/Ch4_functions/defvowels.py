def search4vowels(word: str) -> set:
    """This is documentation string """
    # returns True if any vowels were found in given word
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    # bool returns True if argument is not empty object
    # return bool(found)

    return vowels.intersection(set(word))


print(help(search4vowels))
res1 = search4vowels('navuhodonosor')

print(res1)
word01 = input('Type a word: ')

res2 = search4vowels(word01)
print(res2)
