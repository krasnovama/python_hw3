# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

n = int(input("Введите размер списка: "))
my_list = []
nechet = []
for i in range(0, n):
    my_list.append(random.randint(1, 50))
summa = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        summa = summa + my_list[i]
        nechet.append(my_list[i])
print(
    f'Список: {my_list} \n Элементы, находящиеся на нечетных позициях: {nechet} \n Сумма элементов на нечетных позициях: {summa}')
