import random

messages = ['It is certain', 'It is decidely so', 'Yes definetly', 'Reply hazy try again', 'Ask again later',
            'Concentrate and ask again', 'My reply is no', 'Very doubtful', 'NNNOOOOOO! - luke skywalker']

print(messages[random.randint(0, len(messages) - 1)])
