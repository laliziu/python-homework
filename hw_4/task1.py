# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint

num = int(input('Введите количество элементов первого спика: '))
list_1 = [randint(1, 20) for i in range(num)]
num_2 = int(input('Введите количество элементов второго спика: '))
list_2 = [randint(1, 20) for i in range(num_2)]
print(f' Начальные списки {list_1}, {list_2}')

temp = []
for i in list_1:
    if i not in temp and i in list_2:
        temp.append(i)

print(f' Общие элементы двух списков {temp}')
temp.sort()
print(f' Отсортированный новый список {temp}')


# def list_create_random(begin_num, end_num, length):
#     import random
#     return [random.randint(begin_num, end_num) for _ in range(length)]


# def temp_list(list_1st, list_2nd):
#     temp = []
#     for i in list_1st:
#         if i not in temp and i in list_2nd:
#             temp.append(i)
#     return temp


# len_1st_list = int(input('Enter a number-length for 1st list: '))
# list_1st = list_create_random(1, 20, len_1st_list)

# len_2nd_list = int(input('Enter a number-length for 2nd list: '))
# list_2nd = list_create_random(1, 20, len_2nd_list)


# print(*list_1st)
# print(*list_2nd)
# print(temp_list(list_1st, list_2nd))
