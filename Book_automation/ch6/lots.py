def spam():
    global word
    word = 'damn spammer' #this is global variable

def bacon():
    word = 'pigs meat' #this variable is local

def ham():
    print(word) # this variable is global

word = 'everything'

spam()
print(word)
