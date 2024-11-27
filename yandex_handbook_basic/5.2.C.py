# Классная точка 5.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Согласитесь, что использовать операторы куда удобнее, чем обыкновенные
# методы. Давайте вспомним о реализованном нами методе move(x, y) и напишем
# ему альтернативу в виде операторов + и +=.
# При выполнении кода point + (x, y), создаётся новая точка, которая
# отличается от изначальной на заданное кортежем расстояние по осям x и y.
# При выполнении кода point += (x, y) производится перемещение изначальной точки.
# Напомним, что сейчас мы модернизируем только класс PatchedPoint.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# point = PatchedPoint()
# print(point)
# new_point = point + (2, -3)
# print(point, new_point, point is new_point)
# Вывод
# (0, 0)
# (0, 0) (2, -3) False
# Пример 2
# Ввод
# first_point = second_point = PatchedPoint((2, -7))
# first_point += (7, 3)
# print(first_point, second_point, first_point is second_point)
# Вывод
# (9, -4) (9, -4) True

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

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'

    def __add__(self, point_tuple):
        return self.__class__(self.x + point_tuple[0], self.y + point_tuple[1])

    def __iadd__(self, point_tuple):
        self.x += point_tuple[0]
        self.y += point_tuple[1]
        return self
        

if __name__ == '__main__':
    point = PatchedPoint()
    print(point)
    new_point = point + (2, -3)
    print(point, new_point, point is new_point)

    first_point = second_point = PatchedPoint((2, -7))
    first_point += (7, 3)
    print(first_point, second_point, first_point is second_point)


