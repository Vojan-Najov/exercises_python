# Классная точка 2.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Давайте расширим функционал класса, написанного в прошлой задаче.
# Реализуйте методы:
#     move, который перемещает точку на заданное расстояние по осям x и y;
#     length, который определяет до переданной точки расстояние, округлённое
#             до сотых.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# point = Point(3, 5)
# print(point.x, point.y)
# point.move(2, -3)
# print(point.x, point.y)
# Вывод
# 3 5
# 5 2
# Пример 2
# Ввод
# first_point = Point(2, -7)
# second_point = Point(7, 9)
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


if __name__ == '__main__':

    point = Point(3, 5)
    assert point.x == 3 and point.y == 5
    point.move(2, -3)
    assert point.x == 5 and point.y == 2

    first_point = Point(2, -7)
    second_point = Point(7, 9)
    assert first_point.length(second_point) == 16.76
    assert second_point.length(first_point) == 16.76
