# 2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

numbers = []
for i in range(5):
    numbers.append(random.randint(0, 10))
print(numbers)

count_1 = 0
count_2 = -1
new_list = []

while numbers[count_1] != numbers[count_2]:
    str(new_list.append(numbers[count_1] * numbers[count_2])).split()
    count_1 += 1
    count_2 -= 1
else:
    if numbers[count_1] == numbers[count_2]:
        str(new_list.append(numbers[count_1]* numbers[count_2])).split()

print(new_list)
