#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

# size = int(input('Введите размер списка: '))
# my_list = []
# for i in range(size):
#     my_list.append(random.randint(0, 10))
# print(my_list)
# sum = 0
# count = 0
# for i in my_list:
#     if count % 2 == 1:
#         sum += i
#     count += 1
# print(f'Сумма чисел с нечетными индексами равна = {sum}')


# print(list)
# print(f'Сумма нечетных чисел равна {sum}')



#2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# size = int(input('Введите размер списка: '))
# my_list = []
# for i in range(size):
#     my_list.append(random.randint(0, 10))
# #print(my_list)
# result = []
# for i in range(len(my_list)):
#     while i < len(my_list) / 2 and size > len(my_list) / 2:
#         size = size - 1
#         n = my_list[i] * my_list[size]
#         result.append(n)
#         i += 1
# print(f'{my_list} => {result}')





#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform
#
# size = int(input('Введите размер списка '))
# my_list = []
# for i in range(size):
#     i = uniform(0, 10)
#     my_list.append(round(i, 2))
# print(my_list)
# new_list = []
# for i in my_list:
#     i = i%1
#     new_list.append(round(i,2))
# print(new_list)
#
# min = new_list[0]
# max = 0
# for i in range(len(new_list)):
#         if max < new_list[i]:
#             max = new_list[i]
#         if min > new_list[i]:
#              min = new_list[i]
# dif = max - min
# print(f'max = {max}, min = {min}')
# print(f'Разница между max и min = {(round(dif, 2))}')




#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# a = ''
# n = int(input("Введите десятичное число: "))
# while n > 0:
#     a = str(n%2) + a
#     n = n // 2
# print(f'Двоичная сичисления = {a}')


#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# n = int(input('Введите число: '))
#
# def fibo(n):
#     get_fibo = []
#     a, b = 1, 1
#     for i in range(n-1):
#         get_fibo.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#        get_fibo.insert(0, a)
#        a, b = b, a - b
#     return get_fibo
#
# get_fibo = fibo(n)
# print(fibo(n))
