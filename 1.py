"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

from time import time

some_list = []
some_dict = {}
n = 10 ** 5 # число операций

def time_decorator(func):
    def timer(*args, **Kwargs):
        start = time()
        result = func(*args, **Kwargs)
        end = time()
        print(f'Время выполнения функции {func.__name__} '
              f'составило {end - start}')
        return result

    return timer

@time_decorator
def fill_list_append(lst, num):
    for i in range(num):
        lst.append(i)  # Сложность O(1)

fill_list_append(some_list, n)
print('_' * 100)

@time_decorator
def fill_list_insert(lst, num):
    for i in range(num):
        lst.insert(0, i)  # Сложность O(n)

fill_list_insert(some_list, n)
print('_' * 100)

@time_decorator
def fill_dict(dct, num):
    for i in range(num):  # Сложность O(1)
        dct[i] = i

fill_dict(some_dict, n)
print('_' * 100)

@time_decorator
def change_list(lst):
    for i in range(10000):
        lst.pop(i)           # Сложность O(n)
    for j in range(1000):
        lst[j] = lst[j + 1]  # Сложность O(1)

change_list(some_list)
print('_' * 100)

@time_decorator
def change_dict(dct):
    for i in range(10000):
        dct.pop(i)              # Сложность O(1)
    for j in range(1001, 2002):
        dct[j] = 'fill'         # Сложность O(1)

change_dict(some_dict)
print('_' * 100)