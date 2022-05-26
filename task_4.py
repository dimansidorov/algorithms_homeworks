"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit, repeat

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    result = max(set(array), key=lambda x: array.count(x))
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {array.count(result)} раз(а)'

def func_4():
    return f'Чаще всего встречается число {max(set(array), key=lambda x: array.count(x))}'


print(func_1())
print(repeat('func_1()', repeat=3, globals=globals(), number=100000))
# [0.5151657999958843, 0.4442350000026636, 0.4283274000044912]

print(func_2())
print(repeat('func_2()', repeat=3, globals=globals(), number=100000))
# [0.5451100000063889, 0.5756657999882009, 0.5856817000021692]

print(func_3())
print(repeat('func_3()', repeat=3, globals=globals(), number=100000))
# [0.5446799999917857, 0.534662499994738, 0.5454293999937363]

#print(func_4())
#print(repeat('func_4()', repeat=3, globals=globals(), number=100000))
# [0.44238860000041313, 0.43839090000255965, 0.426019999984419]



'''
func_3() и func_1() дают примерно одинаковое время выполнение кода. func_2() раюотает дольше всех.
На мой вгляд, если учесть факторы читаемости кода и время выполнения, то func_3() будет самая оптимальная из всех.
Сделал еще проверку func_4(). По скорости у нее есть небольшое преимущество в сравнении с func_1(), но и 
функционал у нее неполный.
'''