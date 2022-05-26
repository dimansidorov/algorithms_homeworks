"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit
from random import sample

num_list = sample(range(0, 1000000), 1000)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [num for num, idx in enumerate(nums) if idx % 2 == 0]


print(timeit('func_1(num_list)', globals=globals(), number=10000))
print(func_1(num_list))
print(timeit('func_2(num_list)', globals=globals(), number=10000))
print(func_2(num_list))


'''
Был использован другой подход к этой задаче.
list comprehension работает быстрее, чем классический цикл.
Так же он достаточно легко читаем.
'''