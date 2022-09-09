# 23. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите размер списка: "))
my_list = []
list_rezult = []
for i in range(0, n):
    my_list.append(random.randint(1, 10))
for i in range(len(my_list) // 2):
    list_rezult.append(my_list[i] * my_list[-i - 1])
    print(f'{i + 1} : {my_list[i]}*{my_list[-i - 1]}')
print(f'{my_list}=>{list_rezult}')
