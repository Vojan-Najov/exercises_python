# Классный прямоугольник 2.0
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Расширим функционал класса написанного вами в предыдущей задаче.
# Реализуйте методы:
#     get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
#     get_size() — возвращает размеры в виде кортежа;
#     move(dx, dy) — изменяет положение на заданные значения;
#     resize(width, height) — изменяет размер (положение верхнего левого угла
#                             остаётся неизменным).
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Все результаты вычислений нужно округлить до сотых.
# Пример 1
# Ввод
# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.get_pos(), rect.get_size())
# rect.move(1.32, -5)
# print(rect.get_pos(), rect.get_size())
# Вывод
# (3.2, 3.14) (4.32, 7.44)
# (4.52, -1.86) (4.32, 7.44)
# Пример 2
# Ввод
# rect = Rectangle((7.52, -4.3), (3.2, 3.14))
# print(rect.get_pos(), rect.get_size())
# rect.resize(23.5, 11.3)
# print(rect.get_pos(), rect.get_size())
# Вывод
# (3.2, 3.14) (4.32, 7.44)
# (3.2, 3.14) (23.5, 11.3)

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


if __name__ == '__main__':

    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    assert (rect.get_pos(), rect.get_size()) == ((3.2, 3.14), (4.32, 7.44))

    rect.move(1.32, -5)
    assert (rect.get_pos(), rect.get_size()) == ((4.52, -1.86), (4.32, 7.44))

    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    assert (rect.get_pos(), rect.get_size()) == ((3.2, 3.14), (4.32, 7.44))

    rect.resize(23.5, 11.3)
    assert (rect.get_pos(), rect.get_size()) == ((3.2, 3.14), (23.5, 11.3))
