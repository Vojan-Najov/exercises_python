# Классная точка 3.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Давайте расширим функционал класса, написанного вами в задаче
# «Классная точка 2.0».
# Создайте класс PatchedPoint — наследника уже написанного вами Point.
# Требуется реализовать следующие виды инициализации нового класса:
#     параметров не передано — координаты точки равны 0;
#     передан один параметр — кортеж с координатами точки;
#     передано два параметра — координаты точки.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# point = PatchedPoint()
# print(point.x, point.y)
# point.move(2, -3)
# print(point.x, point.y)
# Вывод
# 0 0
# 2 -3
# Пример 2
# Ввод
# first_point = PatchedPoint((2, -7))
# second_point = PatchedPoint(7, 9)
# print(first_point.length(second_point))
# print(second_point.length(first_point))
# Вывод
# 16.76
# 16.76

class Point():
    
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, other):
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5, 2)

class PatchedPoint(Point):

    def __init__(self, x=0, y=0):
        if isinstance(x, tuple):
            x, y = x[0], x[1]
        super().__init__(x, y)


if __name__ == '__main__':
    point = PatchedPoint()
    print(point.x, point.y)
    point.move(2, -3)
    print(point.x, point.y)

    first_point = PatchedPoint((2, -7))
    second_point = PatchedPoint(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))


