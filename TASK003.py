# 3'. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

# Первое решение:
# import random 
# randomList = [random.randint(1, 10) for i in range(10)]
# print(randomList)

# uniqueElements = []
# for i in range(len(randomList)):
#     if int(randomList[i]) not in uniqueElements:
#         uniqueElements.append(randomList[i])
# print(uniqueElements)

# Решение с улучшением:
from random import randint as rnd

randomList = [rnd(1, 10) for i in range(10)]
print(randomList)
randomList = list(set(randomList))
print(randomList)

