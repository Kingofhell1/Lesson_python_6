# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

min_number = int(input("Введите минимальное число: "))
max_number = int(input("Введите максимальное число: "))
random_list = [randint(1, 30) for i in range(15)]
for i in range(len(random_list)):
    if min_number <= random_list[i] <= max_number:
        print(i)
print(random_list)


