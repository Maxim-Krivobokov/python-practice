import re

# create your own symbol classes with [...]
print('===================vowels==========================')
vowelRegex = re.compile(r'[aeioiAEIOU]')
print(vowelRegex.findall('Robocop eats baby food, BABY FOOD, lol'))


# use ^ to create inverted class
print('===============consonants===========================')
consonantRegex = re.compile(r'[^aeiouAEIOU]')
# this regexp will match all but not aeiou
print(consonantRegex.findall('Robocop eats baby food, BABY FOOD, lol'))


print('===============^ and $===========================')
# ^ symbol means beginning of text
# $ means end
beginwithHello = re.compile(r'^Hello') # Hello at beginning
endsWithNum = re.compile(r'\d$') # one digit at the end
# this will match
print(beginwithHello.findall('Hello world!'))
print(endsWithNum.findall('Your number is 42'))
# this won't match
print(beginwithHello.findall('Say Hello to my little friend!'))
print(endsWithNum.findall('555 is my favoutite number'))


print('===============group symbol . and .* ===========================')

# this regex means 'one symbol'+at
atRegex = re.compile(r'.at')

print(atRegex.findall('The cat in the hat sat on the flat mat, bleat'))

# this will match to all text between 'First Name' and 'Last name', and after 'Last name'. BUT not \n

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

name1 = 'First Name: Akakii Last Name: Pupkin'
name2 = 'First Name: Abdula ibn Mahmud ogly Last Name: Zadov'
print(name1)
print(nameRegex.findall(name1))
print(name2)
print(nameRegex.findall(name2))


print('=======about greediness ===============')
# ? after .* is for non-greedy search
nongreedyRegex = re.compile(r'<.*?>')

greedyRegex = re.compile(r'<.*>')

grtext = '<To serve man> for dinner.>'
print('greedy search:')
print(greedyRegex.findall(grtext))
print('NOTgreedy search:')
print(nongreedyRegex.findall(grtext))

print('======= DOTALL const ===============')
# after adding re.DOTALL symbol '.' will match anything, including \n

nonewLineregex = re.compile('.*')
newLineregex = re.compile('.*', re.DOTALL)

newtext = 'Burn the heretic,\n Kill the mutant. \n Purge the unclean.'

print(newtext)
print('----------without DOTALL-----------')
print(nonewLineregex.search(newtext).group())
print('------------with DOTALL------------:')
print(newLineregex.search(newtext).group())


print('==========IGNORECASE===================')

# adding constant  re.I helps to ignore upper-lower case in text
robocop = re.compile(r'robocop', re.I)

print(robocop.findall('Robocop, robocop, ROBOCOP, RoBoCoP'))

print('================sub()=======================')

# sub() method can replace substring in found text

scpRegex = re.compile(r'Agent \w+')
# Agent and some symbols until space or tab

# first argument - replacing string. Second - source text to find and replace
scptext = scpRegex.sub('DATA EXPUNGED', 'Agent Alice gave the secret documents about scp 685 to Agent Bob.')

print(scptext)

print('---------difficult replcing -----------------')
# two groups of matching
scpRegex2 = re.compile(r'Agent (\w)\w*')

# \1 means first group of matching, = (\w). Agent Alice will be changed to A****
scptext2 = scpRegex2.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Akaki was a double agent')

print(scptext2)