# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input())
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)

# bin(255)
# print(bin)