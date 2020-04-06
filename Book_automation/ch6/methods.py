print('How are you?')
feeling = input()

# answers: gReaT or GREAT or etc. will be the same
if feeling.lower() =='great':
    print('I feel great too.')
else:
    print('I hope you will be ok')

str01 = 'HELLO12'
print(str01.isupper())

#isX methods

# isalpha() - a-Z,A-Z -> true

# isalnum() - a-z, A-Z, 0-9 -> True

# isdecimal() - 0-9 -> True

# isspace()  ' ' -> True

# istitle() Only Words With Captial First Letter ->  True


# startswith(), endswith()

'HelloWorld'.startswith('Hell') # -> true

'HelloWorld'.endswith('World') # -> true

list01 = ['cats', 'rats', 'bats']

print('I like ' + ', '.join(list01))


print('Hello'.rjust(20, '*'))

print('Preved'.ljust(20, '-'))

print('Hola'.center(20, '#'))

#strip(), rstrip(), lstrip() - 