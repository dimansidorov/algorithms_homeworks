"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit

number = int(input('Введите число: '))


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    return str(enter_num)[::-1]


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


print(timeit('revers(number)', globals=globals(), number=1000))
print(timeit('revers_2(number)', globals=globals(), number=1000))
print(timeit('revers_3(number)', globals=globals(), number=1000))
print(timeit('revers_4(number)', globals=globals(), number=1000))


''' 
Из всех предствленных функций я бы сделал выбор в пользу revers_3.
Тема срезов проста, нет лишних строк кода и вложенных функций. 
На выполнение данная функция затрачивает времени меньше всех.
'''