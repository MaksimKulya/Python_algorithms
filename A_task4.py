# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число, ● случайное вещественное число, ● случайный символ. 

# Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import random

r = random()

# a1 = int(input('введите целое число: '))
# a2 = int(input('введите целое число: '))
# b = int(r * (a2-a1+1)) + a1
# print(f'случайное целое число в диапазоне ({a1})--({a2}): {b}')

 
# a1 = float(input('введите вещественное число: \n'))
# a2 = float(input('введите вещественное число: \n'))
# b = r * (a2-a1+1) + a1
# print(f'случайное вещественное число в диапазоне ({a1})--({a2}): {round(b,3)}')


a1 = (input('введите букву из алфавита a-z: \n'))
n1 = ord(a1)
a2 = (input('введите букву из алфавита a-z: \n'))
n2 = ord(a2)
b = int(r * (n2-n1+1)) + n1
print(f'случайная буква в диапазоне ({a1})--({a2}): {chr(b)}')
