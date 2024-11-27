# Стек
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Ещё одной полезной коллекцией является стек реализующий принцип «Последний
# пришёл – первый ушёл». Его часто представляют как стопку карт или магазин
# пистолета, где приходящие элементы закрывают выход уже находящимся в коллекции.
# Реализуйте класс Stack, который не имеет параметров инициализации, но
# поддерживает методы:
#     push(item) — добавить элемент в конец стека;
#     pop() — «вытащить» первый элемент из стека;
#     is_empty() — проверяет стек на пустоту.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# stack = Stack()
# for item in range(10):
#     stack.push(item)
# while not stack.is_empty():
#     print(stack.pop(), end=" ")
# Вывод
# 9 8 7 6 5 4 3 2 1 0 
# Пример 2
# Ввод
# stack = Stack()
# for item in ("Hello,", "world!"):
#     stack.push(item)
# while not stack.is_empty():
#     print(stack.pop())
# Вывод
# world!
# Hello,

class Stack():

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0


if __name__ == '__main__':
    stack = Stack()
    for item in range(10):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop(), end=" ")
    print()
    # 9 8 7 6 5 4 3 2 1 0 

    stack = Stack()
    for item in ("Hello,", "world!"):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop())
    # world!
    # Hello,
