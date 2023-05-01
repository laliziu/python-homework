# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def summ(a, b):
    s = 0
    if a == 0:
        return b
    return (s + summ(a-1, b+1))


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(summ(a, b))
