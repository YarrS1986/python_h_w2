# принимает на вход вещественное число и показывает сумму цифр
# 0,56 -> 11

number = int(input("Введи вещественное число -> ").replace(',', '').replace('-', '').replace('.', ''))
sum_num = 0
new_number = str(number)
for i in range(len(new_number)):
    sum_num += int(new_number[i])

print(sum_num)