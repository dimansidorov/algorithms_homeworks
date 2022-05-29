"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

lst = [i for i in range(1000)]
deq = deque([i for i in range(1000)])


print(f"list - {timeit('[i for i in range(1000)]', globals=globals(), number=10000)}")  # 0.7722427999979118
print(f"deque - {timeit('deque([i for i in range(1000)])', globals=globals(), number=10000)}")  # 0.9624405999966257


# 1. сравнить операции append, pop, extend списка и дека и сделать выводы что и где быстрее.
def append_func(some_list, num=10):
      for i in range(num):
            some_list.append(i)

      return some_list


def pop_func(some_list, num=10):
      for i in range(num):
            some_list.pop()
      return some_list


def extend_func(some_list, num=10):
      for i in range(num):
            some_list.extend([i, i + 1])
      return some_list


print(f"list.append() - {timeit('append_func(lst)', globals=globals(), number=10000)}")   # 0.18852139999944484
print(f"deque.append() - {timeit('append_func(deq)', globals=globals(), number=10000)}")     # 0.18886579999889364
print(f"list.pop() - {timeit('pop_func(lst)', globals=globals(), number=10000)}")  # 0.024270799999840165
print(f"deque.pop() - {timeit('pop_func(deq)', globals=globals(), number=10000)}")     # 0.019788600000083534
print(f"list.extend() - {timeit('extend_func(lst)', globals=globals(), number=10000)}")   # 0.044566999999915424
print(f"deque.extend() - {timeit('extend_func(deq)', globals=globals(), number=10000)}")  # 0.041039299999965806

'''
Методы из первого пункта работают в list и deque одинаково, либо разница незначительна.
'''

# 2. сравнить операции appendleft, popleft, extendleft дека и соответствующих
# им операций списка и сделать выводы что и где быстрее


def insert_into(some_list, num=10):
      if isinstance(some_list, list):
            for i in range(num):
                  some_list.insert(0, 1)
      else:
            for j in range(num):
                  some_list.appendleft(1)

      return some_list


def pop_to(some_list, num=10):
      if isinstance(some_list, list):
            for i in range(num):
                  some_list.pop(0)
      else:
            for j in range(num):
                  some_list.popleft()
      return some_list


def extend2(some_list, num=100):
      if isinstance(some_list, list):
            for i in range(num):
                  new = [i, i + 1]
                  new.extend(some_list)
                  some_list = new
      else:
            for j in range(num):
                  some_list.extendleft([j, j + 1])
      return some_list

print(f"list.insert(0, 1) - {timeit('insert_into(lst)', globals=globals(), number=10000)}")   # 4.759982599999603
print(f"deque.appendleft(1) - {timeit('insert_into(deq)', globals=globals(), number=10000)}")     # 0.022300300000097195
print(f"list.pop(0) - {timeit('pop_to(lst)', globals=globals(), number=10000)}")  # 2.7687700999999834
print(f"deque.popleft() - {timeit('pop_to(deq)', globals=globals(), number=10000)}")     # 0.022032899999885558
print(f"extend(list) - {timeit('extend2(lst)', globals=globals(), number=10000)}")   # 5.701962000000094
print(f"deque.extendleft() - {timeit('extend2(deq)', globals=globals(), number=10000)}")   # 0.4143757000001642

'''
Операции по добавлению в начало списков показают большую разницу в скорости выполнения.
Если имеется необходимость добавлять в начало списка и конец списка одновременно, то deque имеет большое преимущество.
'''

# 3. сравнить операции получения элемента списка и дека и сделать выводы что и где быстрее


def show_el(some_list, num=100):
      for i in range(num):
            some_list[i] = i
      return some_list


print(f"list[el] - {timeit('show_el(lst)', globals=globals(), number=100000)}")     # 0.9715781999998399
print(f"deque[el] - {timeit('show_el(deq)', globals=globals(), number=100000)}")    # 1.1478624999999738


'''
операции получения элемента списка работают быстрее, чем анологичные операции в deque
'''



