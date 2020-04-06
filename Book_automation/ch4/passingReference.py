def dobavka(someParameter):
    someParameter.append('Hello')


words = ['preved', 'hi', 'ola']
dobavka(words)
# someparameter takes a link to list, modifies it, and printing list words  shows changes

print(words)
