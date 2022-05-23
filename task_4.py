"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
from hashlib import sha512

salt = 'some_salt'
storage = {}


def read_or_write(url_string):
    if url_string in storage:
        return storage[url_string]
    else:
        storage[url_string] = sha512(url_string.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        return f'Хэш url: {url_string} записан'


print(read_or_write('vk.com'))
print(read_or_write('vk.com'))
print(read_or_write('yandex.ru'))
print(read_or_write('yandex.ru'))
print(read_or_write('tinkoff.ru'))
print(read_or_write('tinkoff.ru'))


