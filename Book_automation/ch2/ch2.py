print('Enter your name pls')
name = input()

print('enter your age pls')
age = input()


if name == 'Vasya':
    print('Hi, Vasya.')
elif int(age) < 18:
    print('go away schoolota')
elif int(age) > 2000:
    print('Im going to call Blade, vampire.')
elif int(age) > 100:
    print('too old for lego')
else:
    print('you are not vasya, not vampire, not a kid. Who are you?')
