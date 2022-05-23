"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
from hashlib import sha512
import mysql.connector
import mysql.connector.errors


# DROP DATABASE IF EXISTS homework3;
# CREATE DATABASE homework3;
# делал с mysql, так как нас учили на ней и она у меня стоит.

# функция для распаковки
def unpack(value, depth=0):
    if depth and isinstance(value, list):
        for v in value:
            return unpack(list(v), depth - 1)
    else:
        return ''.join(value)

try:
    password = input('Введите пароль для подключения к MySQL ')
    my_db = mysql.connector.connect(host='localhost',
                                    user='root',
                                    password=password,
                                    port='3306',
                                    database='homework3')

except mysql.connector.errors.ProgrammingError:
    print('Что-то пошло не так. Перезапустите программу.')

else:
    cursor = my_db.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS users;")

    cursor.execute("CREATE TABLE users(id SERIAL PRIMARY KEY, "
                   "username VARCHAR(50) UNIQUE NOT NULL, password_hash VARCHAR(150) NOT NULL);")

    username = input('Введите username: ')
    password = input('Введите пароль: ')
    hash_password = sha512(password.encode('utf-8') + username.encode('utf-8')).hexdigest()
    cursor.execute(f"INSERT INTO users(username, password_hash)"
                   f"VALUES ('{username}', '{hash_password}');")

    cursor.execute(f"SELECT password_hash FROM users "
                   f"WHERE username = '{username}';")

    password_from_bd = unpack(cursor.fetchall(), 2)     # Просто для себя изучал функции модуля

    password = input('Введите пароль еще раз: ')
    hash_password = sha512(password.encode('utf-8') + username.encode('utf-8')).hexdigest()
    try:
        assert password_from_bd == hash_password

    except AssertionError:
        print('Введенный повторно пароль не совпадает')

    else:
        print('Вы ввели правильный пароль')