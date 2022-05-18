"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def show_elements(self):
        return self.elems

class TaskBoard:

    def __init__(self):
        self.basic = QueueClass()
        self.unresolved = QueueClass()
        self.resolved = QueueClass()

    def to_basic(self):
        self.basic.to_queue()

    def from_basic_to_unresolved(self):
        self.unresolved.to_queue(self.basic.from_queue())


    def from_basic_to_resolved(self):
        self.resolved.to_queue(self.basic.from_queue())

    def from_unresolved_to_resolved(self):
        self.resolved.to_queue(self.unresolved.from_queue())

if __name__ == '__main__':

    board = TaskBoard()
    print(f'Колличество задач: {board.basic.size()}. \n'
          f'Колличество отложенных или нерешенных задач: {board.unresolved.size()}. \n'
          f'Колличество решенных задач: {board.resolved.size()}')
    print(*(['*' for _ in range(30)]))

    board.basic.to_queue('Сдать ДЗ по Питону вовремя!!!')
    board.basic.to_queue('Сходить в магазин')
    board.basic.to_queue('Сходить к врачу')

    print(f'Колличество задач: {board.basic.size()}. \n'
          f'Колличество отложенных или нерешенных задач: {board.unresolved.size()}. \n'
          f'Колличество решенных задач: {board.resolved.size()}')
    print(f'Задачи: {board.basic.show_elements()}.\n'
          f'Отложенные или нерешенные задачи: {board.unresolved.show_elements()}. \n'
          f'Решенные задачи: {board.unresolved.show_elements()}.')
    print(*(['-' for _ in range(30)]))

    board.from_basic_to_unresolved()
    board.from_basic_to_resolved()

    print(f'Колличество задач: {board.basic.size()}. \n'
          f'Колличество отложенных или нерешенных задач: {board.unresolved.size()}. \n'
          f'Колличество решенных задач: {board.resolved.size()}')
    print(f'Задачи: {board.basic.show_elements()}. \n'
          f'Отложенные или нерешенные задачи: {board.unresolved.show_elements()}. \n'
          f'Решенные задачи: {board.resolved.show_elements()}.')
    print(*(['/' for _ in range(30)]))

    board.from_unresolved_to_resolved()
    board.from_basic_to_unresolved()


    print(f'Колличество задач: {board.basic.size()}. \n'
          f'Колличество отложенных или нерешенных задач: {board.unresolved.size()}. \n'
          f'Колличество решенных задач: {board.resolved.size()}')
    print(f'Задачи: {board.basic.show_elements()}.\n'
          f'Отложенные или нерешенные задачи: {board.unresolved.show_elements()}. \n'
          f'Решенные задачи: {board.resolved.show_elements()}.')
    print(*(['+' for _ in range(30)]))