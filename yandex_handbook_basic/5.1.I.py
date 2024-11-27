# Очередь
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# В программировании существует потребность не только в изученных нами
# коллекциях. Одна из таких очередь. Она реализует подход к хранению данных по
# принципу «Первый вошёл – первый ушел».
# Реализуйте класс Queue, который не имеет параметров инициализации, но
# поддерживает методы:
#     push(item) — добавить элемент в конец очереди;
#     pop() — «вытащить» первый элемент из очереди;
#     is_empty() — проверят очередь на пустоту.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# queue = Queue()
# for item in range(10):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop(), end=" ")
# Вывод
# 0 1 2 3 4 5 6 7 8 9 
# Пример 2
# Ввод
# queue = Queue()
# for item in ("Hello,", "world!"):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop())
# Вывод
# Hello,
# world!

class Queue():
    
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0


if __name__ == '__main__':
    queue = Queue()
    for item in range(10):
        queue.push(item)
    while not queue.is_empty():
        print(queue.pop(), end=" ")
    print()

    queue = Queue()
    for item in ("Hello,", "world!"):
        queue.push(item)
    while not queue.is_empty():
        print(queue.pop())
