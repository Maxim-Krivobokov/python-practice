import random

# Считаем сумму всех чисел от 0 до 100, или больших
total = 0
for num in range(101):
    total = total + num
print(total)


for i in range(10):
    print(random.randint(1, 100))
