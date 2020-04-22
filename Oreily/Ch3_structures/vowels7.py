
#vowels = {'a', 'e', 'i', 'o', 'u'}

# better way to create a set
vowels = set('aeiou')

word = input('Provide a word to search for vowels. \n')

found = vowels.intersection(set(word))


for vowel in found:
    print(vowel)
