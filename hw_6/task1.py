#  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a_1 = int(input('Введите первый элемент: '))
n = int(input('Введите количество элементов: '))
d = int(input('Введите разность элементов: '))

print(f' n-ый член прогрессии: {a_1 +(n-1) * d}')