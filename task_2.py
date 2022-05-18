"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""
from random import randint


numbers = [randint(-1000, 1000) for i in range(20)]


# O(n^2). Честно говоря ничего не придумал, кроме как создать ненужный второй цикл.
def min_number_1(lst):
    minimum = lst[0]  # O(1)
    for i in range(len(lst)):   # O(n)
        for j in lst:           # O(n)
            if j < minimum:     # O(1)
                minimum = j     # O(1)
    return f'Минимальное число из списка = {minimum}'         # O(1)


# O(n)
def min_number_2(lst):
    minimum = lst[0]    # O(1)
    for i in lst[1:]:   # O(n)
        if i < minimum:  # 0(1)
            minimum = i     # O(1)
    return f'Минимальное число из списка = {minimum}'      # O(1)


print(min_number_1(numbers))
print(min_number_2(numbers))
print(min(numbers))