# 24. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input("Введите размер списка: "))
my_list = []
for i in range(0, n):
    my_list.append(round(random.uniform(1, 10), 2))
min = my_list[0]
max = my_list[0]
for i in range(len(my_list)):
    if my_list[i] < min:
        min = my_list[i]
    elif my_list[i] > max:
        max = my_list[i]
print(f'{my_list} => {round(min % 1, 2)} * {round(max % 1, 2)} = {round(min % 1 * max % 1, 2)}')
