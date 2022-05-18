"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StacksOfDishes:

    def __init__(self):
        self.dishes = [[]]
        self.max = 5

    def __len__(self):
        return len(self.dishes)

    def is_empty(self):
        return self.dishes == [[]]

    def put_on(self, element):
        if len(self.dishes[-1]) >= self.max:
            new_bunch = [element]
            self.dishes.append(new_bunch)
        else:
            self.dishes[-1].append(element)

    def put_out(self):
        if len(self.dishes[-1]) == 1:
            self.dishes = self.dishes[:-1]
        else:
            self.dishes[-1] = self.dishes[-1][:-1]

    def last_bunch(self):
        return len(self.dishes[-1])

if __name__ == '__main__':

    some_stacks = StacksOfDishes()
    print(f'Test 1: {some_stacks.is_empty()}')

    for i in range(26):
        some_stacks.put_on(i)

    print(f'Test 2: {some_stacks.is_empty()}')
    print(len(some_stacks))
    print(f'В последней стопке {some_stacks.last_bunch()} тарелок.')
    for i in range(6):
        some_stacks.put_out()

    print(f'Test 3: {some_stacks.is_empty()}')
    print(len(some_stacks))
    print(f'В последней стопке {some_stacks.last_bunch()} тарелок.')