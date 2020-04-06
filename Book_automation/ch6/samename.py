def spam():
    print(word) # this will cause an error
    word = 'some spam'

word = 'global'
spam()