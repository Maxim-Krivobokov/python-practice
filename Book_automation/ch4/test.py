name = 'Navuhodonosor'

for i in name:
    print('* * * ' + i + ' * * *')

# you can not modify a string, just create a new one
sentence = 'Basrsik is a cat'
print(sentence.index(' a '))
new_sent = sentence[0:10] + ' the ' + sentence[12:]

print(new_sent)
