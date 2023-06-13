from random import randint, choice
import random

random.seed(0)

qnt = 100
list = [0]

for i in range(qnt):
    new_num = randint(list[i] - 1, list[i] + 1)
    list.append(new_num)
print(list)