'''Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
 В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

a = [int(i) for i in input("Введите список: ").split()]
b = int(input("Введите число: "))
number = 0
for i in range(len(a)):
    if (b-a[i]) < b-number and b-a[i] > 0:
        number = i
print(a[number])
