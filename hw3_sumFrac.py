# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.


n = int(input('Введи значение n = '))
my_list = [(1 + 1 / i) ** i for i in range(1, n + 1)]
print('Сумма:{}'.format(round(sum(my_list), 2)))