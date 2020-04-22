found = {}

vowels = ['i', 'o', 'u', 'a', 'e']

for i in vowels:
    found[i] = 0

print('empty dict:')
print(found)
print(' ')

word = input('Enter a word. \n')

for letter in word:
    if letter.lower() in vowels:
        found[letter.lower()] += 1


print('result sorted dict:')
print(sorted(found))

# for key in sorted(found):
# print(key + ' was found ' + str(found[key]) + ' times')    # not perfect way to print dict

for key, value in sorted(found.items()):
    print(key, ' was found ', value, ' times.')
