# 5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring

from gbfunction import give_int

a = give_int("Введите число: ")
print(a)

fibonachi = []
number_1 = 0
number_2 = 1
x = -1
for i in range(a):
    fibonachi.insert(0, number_1 * x) 
    fibonachi.append(number_1)
    x = x * (-1)
    number_1, number_2 = number_2, number_1 + number_2 

fibonachi.pop(len(fibonachi)//2)
print(fibonachi)