# Реализуйте алгоритм перемешивания списка

len_list = int(input('Введи длину массива = '))

# 1. ввод элементов массива вручную
# old_list = [int(input(f'Введи {i} элемент массива = ')) for i in range(1, len_list+1)]

# 2. ввод элементов рандомом
import random

old_list = [random.randint(1, 99) for i in range(1, len_list + 1)]

new_list = random.sample(old_list, len_list)

print(f'{old_list} -> {new_list}')