"""#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:  6782 -> 23           0,56 -> 11 
number = input("Введите вещественное число: ")
summa=0
for i in number:
    if i.isdigit():
        summa+=int(i)
print(summa)

"""

num = input("Введите вещественное число: ").replace('.', '').replace(',', '')
result = sum([int(item) for item in num])
print(f'{num} -> {result}')