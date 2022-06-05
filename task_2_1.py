"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint, seed
from timeit import timeit

seed(1)


def shell_sort(lst):
    inc = len(lst) // 2
    while inc:
        for i, el in enumerate(lst):
            while i >= inc and lst[i - inc] > el:
                lst[i] = lst[i - inc]
                i -= inc
            lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return lst


def median_(lst):
    index = len(lst) // 2
    if len(lst) % 2:
        return shell_sort(lst)[index]

    return sum(shell_sort(lst)[index - 1:index + 1]) / 2


m = 10
ten = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана массива из 10 элементов - {median_(ten)}')
print(f'Замер функции поиска медиана в массиве длиной 10: '
      f'{timeit("median_(ten[:])",globals=globals(),number=1000)}')    # 0.00831629999447614


m = 100
hundred = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана массива из 100 элементов - {median_(hundred)}')
print(f'Замер функции поиска медиана в массиве длиной 100: '
      f'{timeit("median_(hundred[:])",globals=globals(),number=1000)}')    # 0.1549352000001818


m = 1000
thousand = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана массива из 1000 элементов - {median_(thousand)}')
print(f'Замер функции поиска медиана в массиве длиной 1000: '
      f'{timeit("median_(thousand[:])",globals=globals(),number=1000)}')    # 2.5749117999803275

