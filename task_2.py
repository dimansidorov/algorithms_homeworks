"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from functools import reduce
from collections import defaultdict

titles = ['Первый элемент', 'Второй элемент']


def sum_of_numbers():
    numbers = defaultdict(list)
    for i in titles:
        numbers[i] = list(input(f'Введите {i.lower()} '))
    result = hex(sum([int(''.join(num), base=16) for num in numbers.values()]))
    return f'Сумма двух шестнадцетиричных чисел = {list(result[2:].upper())}'


def multi_of_numbers():
    numbers = defaultdict(list)
    for i in titles:
        numbers[i] = list(input(f'Введите {i.lower()}'))
    result = hex(reduce(lambda x, y: x * y, [int(''.join(num), base=16) for num in numbers.values()]))
    return f'Произведение двух шестнадцетиричных чисел = {list(result[2:].upper())}'


print(sum_of_numbers())
print(multi_of_numbers())