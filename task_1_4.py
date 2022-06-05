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

Это файл для четвертого скрипта
"""
# задача из урока 5 про предприятия.
from collections import namedtuple
from recordclass import recordclass
from pympler import asizeof


# Старый вариант.
def append_to_ntuple():
    try:
        num = int(input('Введите количество предприятий для расчета прибыли: '))
        companies = []
        ntuple = namedtuple('company', 'title profit')
        for i in range(num):
            title = input('Введите название предприятия: ')
            profit = [int(i) for i in input('через пробел введите прибыль данного предприятия '
                                            'за каждый квартал(Всего 4 квартала):').split()]
            company = ntuple(title, sum(profit))
            companies.append(company)
    except ValueError:
        print('Вы ввели неверное значение. Перезапустите программу.')
        return
    else:
        return companies


def avg_func(lst):
    avg_profit = sum([l.profit for l in lst])/len(lst)
    high_avg = [k.title for k in lst if k.profit >=
                avg_profit]
    low_avg = [x.title for x in lst if x.profit < avg_profit]
    return f'Средняя годовая прибыль всех предприятий: {avg_profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {", ".join(high_avg)}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {", ".join(low_avg)}'


company_lst = append_to_ntuple()
a = asizeof.asizeof(company_lst)
print(a)     # 440
# print(avg_func(company_lst))


# Новый вариант
def append_to_rtuple():
    try:
        num = int(input('Введите количество предприятий для расчета прибыли: '))
        companies = []
        rtuple = recordclass('company', 'title profit')
        for i in range(num):
            title = input('Введите название предприятия: ')
            profit = [int(i) for i in input('через пробел введите прибыль данного предприятия '
                                            'за каждый квартал(Всего 4 квартала):').split()]
            company = rtuple(title, sum(profit))
            companies.append(company)
    except ValueError:
        print('Вы ввели неверное значение. Перезапустите программу.')
        return
    else:
        return companies


rec_company_lst = append_to_rtuple()
b = asizeof.asizeof(rec_company_lst)
print(b)     # 152
# print(avg_func(company_lst))

print(f'Namedtuple расходует памяти больше, чем recordclass в {a / b} раз.')

'''
Recordclass очень здорово оптимизирует память.
'''