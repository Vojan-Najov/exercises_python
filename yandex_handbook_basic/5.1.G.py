# Классный прямоугольник 3.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Необходимо ещё немного доработать предыдущую задачу.
# Разработайте методы:
#     turn() — поворачивает прямоугольник на 90° по часовой стрелке вокруг его
#              центра;
#     scale(factor) — изменяет размер в указанное количество раз, тоже
#              относительно центра.
# Все вычисления производить с округлением до сотых.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.turn()
# print(rect.get_pos(), rect.get_size(), sep='\n')
# Вывод
# (-3.14, 2.71)
# (6.28, 5.42)
# (-2.71, 3.14)
# (5.42, 6.28)
# Пример 2
# Ввод
# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.scale(2.0)
# print(rect.get_pos(), rect.get_size(), sep='\n')
# Вывод
# (-3.14, 2.71)
# (6.28, 5.42)
# (-6.28, 5.42)
# (12.56, 10.84)

def rounder(prec=0):
    def decorated_1(func):
        def decorated_2(*args):
            nonlocal prec
            return round(func(*args), prec)
        return decorated_2
    return decorated_1


class Rectangle():

    def __init__(self, point1, point2):
        self.point = min(point1[0], point2[0]), max(point1[1], point2[1])
        self.width = abs(point1[0] - point2[0])
        self.height = abs(point1[1] - point2[1])

    @rounder(2)
    def perimeter(self):
        return 2 * (self.width + self.height)

    @rounder(2)
    def area(self):
        return self.width * self.height

    def get_pos(self):
        return round(self.point[0], 2), round(self.point[1], 2)

    def get_size(self):
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx, dy):
        self.point = (self.point[0] + dx, self.point[1] + dy)

    def resize(self, width, height):
        self.width = width
        self.height = height

    def turn(self):
        centre = self.point[0] + self.width / 2, self.point[1] - self.height / 2
        self.width, self.height = self.height, self.width
        self.point = centre[0] - self.width, centre[1] - self.height


if __name__  == '__main__':

    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    assert (rect.get_pos(), rect.get_size()) == ((-3.14, 2.71), (6.28, 5.42))
# rect.turn()
# print(rect.get_pos(), rect.get_size(), sep='\n')
# Вывод
# (-2.71, 3.14)
# (5.42, 6.28)
# Пример 2
# Ввод
# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.scale(2.0)
# print(rect.get_pos(), rect.get_size(), sep='\n')
# Вывод
# (-3.14, 2.71)
# (6.28, 5.42)
# (-6.28, 5.42)
# (12.56, 10.84)
