# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# my_list = [1, 2, 1, 1, 2, 2, 1, 2]
# print(my_list)
# o = 1
# r = 2
# i = 0

# while my_list < (len -1):
#     if my_list[i] == 1:
#         i+=1
#     else:
#         my_list[i]= 1

# print(my_list)

number = int(input('How many coins? '))
count_0 = 0
count_1 = 0
for i in range(number):
    coin = int(input(' Enter 1 or 0:'))
    if count_0 == 0:
        count_0 += 1
        if count_0 < count_1:
            countMin = count_0
    else:
        countMin = count_1
        print('{} min coins need to fleep'.format(countMin))
