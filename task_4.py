"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


dict1 = {i: i**2 for i in range(1000)}
dict2 = OrderedDict([(i, i**2) for i in range(1000)])

print(timeit('{i: i**2 for i in range(1000)}', globals=globals(), number=1000))     # 0.5408291999992798
print(timeit('OrderedDict([(i, i**2) for i in range(1000)])', globals=globals(),
             number=1000))      # 0.9376011999993352

print(timeit('dict1[1] = 0', globals=globals(), number=100000))     # 0.012192400000003545
print(timeit('dict2[1] = 0', globals=globals(), number=100000))    # 0.017487900000105583

print(timeit('dict1[1]', globals=globals(), number=1000000))     # 0.11036350000040329
print(timeit('dict2[1]', globals=globals(), number=1000000))     # 0.11307469999974273

'''
На мой вгляд смысла использовать OrderedDict в версиях старше 3.6 нет.
'''





