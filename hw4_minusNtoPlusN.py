# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

num = int(input("Введи число N = "))
lst1 = [0]
lst2 = []

i = 1
while i <= num:
    lst1.append(i)
    lst2.append(i*-1)
    i += 1
lst2.reverse()
lst_sum = lst2+lst1
print(lst_sum)

print("Выбери номер позиции (индекса) элемента списка, где первый индекс = 0")
human_choise1 = int(input("Введи позицию(индекс) № 1: "))
human_choise2 = int(input("Введи позицию(индекс) № 2: "))
composition = lst_sum[human_choise1] * lst_sum[human_choise2]
print(composition)