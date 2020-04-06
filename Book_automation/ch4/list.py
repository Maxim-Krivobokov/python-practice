list01 = ['cat', 'dog', 'mice', 'tiger', 'elephant', 'fox', 'wolf']

list02 = [['bmw', 'mercedes', 'audi'], ['m5', 'e55amg', 'rs6']]


gcars = ['bmw', 'porsche', 'opel']

jcars = ['toyota', 'honda', 'subaru']
print(list01[0])

print(list02[0][0])


# print(list01[-1])

# print(list02[1][:2])

# print(len(list01))

# print(len(list02))

# concatenating two lists
print(jcars + gcars)

# printing one list threree times
#print(list01 * 3)

# removing item from list
del gcars[2]

print(gcars)
