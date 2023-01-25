"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
элементов списка, стоящих на позиции с нечетным индексом.

Предыдущее решение:
num = [2, 3, 5, 9, 3]
def sum_odd_index(num):
    sum = 0
    for i in range(len(num)):
        if i % 2 != 0:
            sum += num[i]
    print(f"Сумма на нечётных позициях: {sum}")

sum_odd_index(num)

"""


from random import randint as ri

num_list = [ri(1, 10) for _ in range(ri(5, 10))]
total = sum([num_list[i] for i in range(1, len(num_list), 2)])
print(f'Созданный список: {num_list}\nСумма элементов на позиции с нечетным индексом: {total}')