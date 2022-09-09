# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("Введите число: "))
my_list = [1, 1]
neg_my_list = [-1, -1]
negative = []
feb_list = []
for i in range(2, k):
    my_list.append(my_list[i - 1] + my_list[i - 2])
    neg_my_list.append(neg_my_list[i - 1] + neg_my_list[i - 2])
for i in range(len(neg_my_list) - 1, -1, -1):
    negative.append(neg_my_list[i])
feb_list = [*negative, 0, *my_list]
print(feb_list)
