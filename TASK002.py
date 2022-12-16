# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Первое решение:
# newList = [2, 3, 4, 5, 6]
# product = []
# l = len(newList)
# for i in range(int(l/2 + 0.5)):
#     product.append(newList[i] * (newList[l - 1 - i]))
# print(product)

# Улучшение:
newList = [2, 3, 4, 5, 6]
newList = [newList[i]*newList[i *(-1)-1] for i in range(len(newList))]
newList = newList[0:int(len(newList)/2 + 0.5):1]
print(newList)