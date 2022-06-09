"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

'''
Пример разобрал, но пошло тяжеловато. Буду прорабатывать его позднее.
'''
from collections import Counter, deque


def haffman_tree(string):
    unique_symbols = Counter(string)
    sorted_unique_symbols = deque(sorted(unique_symbols.items(), key=lambda x: x[1]))
    if len(sorted_unique_symbols) != 1:
        while len(sorted_unique_symbols) > 1:
            accumulated = sorted_unique_symbols[0][1] + sorted_unique_symbols[1][1]
            joint_elem = {0: sorted_unique_symbols.popleft()[0],
                    1: sorted_unique_symbols.popleft()[0]}
            for idx, count in enumerate(sorted_unique_symbols):
                if accumulated > count[1]:
                    continue
                else:
                    sorted_unique_symbols.insert(idx, (joint_elem, accumulated))
                    break
            else:
                sorted_unique_symbols.append((joint_elem, accumulated))
    else:
        accumulated = sorted_unique_symbols[0][1]
        joint_elem = {0: sorted_unique_symbols.popleft()[0], 1: None}
        sorted_unique_symbols.append((joint_elem, accumulated))

    return sorted_unique_symbols[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


message = input('Введите строку для кодирования: ')

haffman_code(haffman_tree(message))

for i in message:
    print(code_table[i], end=' ')
