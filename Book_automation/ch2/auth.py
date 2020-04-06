while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello ,Joe. Enter you password.')
    password = input()
    if password == 'tits':
        break

print('Acess Granted')
