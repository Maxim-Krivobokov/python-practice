test1 = [2, 4, 6, 8, 10, 12]

test1[2] = 'qwer'

print(test1)

test2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# test2[int('3' * 2) / 11] - causes an error, because float index


def funct1(words):   # writing all elements into one string, adding "and" before last one
    result = words[0]
    endword = int(len(words) - 1)
    for word in words[1:endword]:  # using slice to awoid adding ", " before first word
        result = str(result + ', ' + word)
    result = str(result + ' and ' + words[-1])
    return result


food = ['apples', 'bananas', 'tofu', 'oats']

print(funct1(food))
# print(result)
