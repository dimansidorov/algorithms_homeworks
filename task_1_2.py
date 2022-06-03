"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""
# Задача про уникальные подстроки из данного курса.
from numpy import array
from hashlib import sha256
from pympler import asizeof


def unique_hash_substring(*args):
    result = set()
    for substring in substrings:
        result.add(sha256(substring.encode('utf-8')).hexdigest())

    return result


# мой вариант из дз 3
string = 'papararapapa'
# string = 'papararapapararapapa'
substrings = [string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1) if string[i: j] != string]
a = asizeof.asizeof(substrings)
print(f'Память list - {a}')     # 4712


# новый вариант
substrings = array([string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1) if string[i: j] != string])
b = asizeof.asizeof(substrings)
print(f'Память array from numpy - {b}')
print(f'array из библиотеки numpy занимает {round(b / a, 3)} от такого же массива типа list')
#print(*unique_hash_substring(substrings), sep='\n')

'''
array надо использовать аккуратно, т.к. во втором варианте строки array занимает больше памяти, чем list
'''
