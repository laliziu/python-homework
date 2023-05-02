# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

num = int(input('Введите кол-во элементов: '))
my_list = [randint(1,100) for i in range(num)]
print(my_list)

temp = []

minn = int(input('Диапозон от: '))
maxx = int(input('До: '))

for i in range(len(my_list)):
    if my_list[i] > minn and my_list[i] < maxx:
        temp.append(i)

print(f'Индексы элементов {temp}')
