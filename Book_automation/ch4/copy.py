import copy
# copy() function cretes a real copy of a list or vocabilary

# deepcopy() for copying lists of lists

words = ['preved', 'ola', 'chao', 'hello']
spam = [1, 2, 3, 4, 5]
slova = copy.copy(spam)  # ???

slova[1] = 'Zdorovenki buly'

print(words)
print(slova)
