"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
from hashlib import sha256


def unique_hash_substring(*args):
    result = set()
    for substring in substrings:
        result.add(sha256(substring.encode('utf-8')).hexdigest())

    return result


string = input('Введите строку для построения подстрок: ')
substrings = [string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1) if string[i: j] != string]

print(*unique_hash_substring(substrings), sep='\n')