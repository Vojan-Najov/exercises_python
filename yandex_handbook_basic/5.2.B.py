# Классная точка 4.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# А теперь модернизируем уже новый класс PatchedPoint. Реализуйте магические
# методы _str_ и _repr_.
# При преобразовании в строку точка представляется в формате (x, y).
# Репрезентация же должна возвращать строку для инициализации точки двумя
# параметрами.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# point = PatchedPoint()
# print(point)
# point.move(2, -3)
# print(repr(point))
# Вывод
# (0, 0)
# PatchedPoint(2, -3)
# Пример 2
# Ввод
# first_point = PatchedPoint((2, -7))
# second_point = PatchedPoint(7, 9)
# print(*map(str, (first_point, second_point)))
# print(*map(repr, (first_point, second_point)))
# Вывод
# (2, -7) (7, 9)
# PatchedPoint(2, -7) PatchedPoint(7, 9)

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
        

if __name__ == '__main__':
    point = PatchedPoint()
    print(point)
    point.move(2, -3)
    print(repr(point))

    first_point = PatchedPoint((2, -7))
    second_point = PatchedPoint(7, 9)
    print(*map(str, (first_point, second_point)))
    print(*map(repr, (first_point, second_point)))


