import time

def calcProd():
    # counting composition of 0 to 10000
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()

prod = calcProd()
endTime = time.time()

print('Result of composition first 100000 is number with length = %s characters.' % (len(str(prod))))
print('Calculating tooc %s seconds.' % (endTime - startTime))
