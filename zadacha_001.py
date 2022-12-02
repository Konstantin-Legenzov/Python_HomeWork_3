# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

numbers = []
for i in range(3):
    numbers.append(random.randint(0,10))
print(numbers)
sum = 0

for count in range(1, len(numbers), 2):
    sum += numbers[count]
print(sum)