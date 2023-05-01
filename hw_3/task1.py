#  Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

print("Наш массив")
my_list = [randint(1, 10) for i in range(10)]
print(my_list)

number = int(input("Ищем число: "))
count = 0

for i in range(10):
    if my_list[i] == i:
        count += 1
print(f'Число {number} встречается в массиве {count} раза')

if number not in my_list:
    print("Такого числа в массиве нет")
