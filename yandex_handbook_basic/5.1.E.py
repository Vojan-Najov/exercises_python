# Классный прямоугольник
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Давайте перейдём к более сложным геометрическим фигурам.
# Разработайте класс Rectangle.
# При инициализации класс принимает два кортежа рациональных координат
# противоположных углов прямоугольника (со сторонами параллельными осям
# координат).
# Класс должен реализовывать методы:
#     perimeter — возвращает периметр прямоугольника;
#     area — возвращает площадь прямоугольника.
# Все результаты вычислений нужно округлить до сотых.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.perimeter())
# Вывод
# 23.52
# Пример 2
# Ввод
# rect = Rectangle((7.52, -4.3), (3.2, 3.14))
# print(rect.area())
# Вывод
# 32.14

def rounder(prec=0):
    def decorated_1(func):
        def decorated_2(*args):
            nonlocal prec
            return round(func(*args), prec)
        return decorated_2
    return decorated_1


class Rectangle():

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    @rounder(2)
    def perimeter(self):
        return 2 * (abs(self.point1[0] - self.point2[0]) +
                abs(self.point1[1] - self.point2[1]))

    @rounder(2)
    def area(self):
        return abs(self.point1[0] - self.point2[0]) * \
                abs(self.point1[1] - self.point2[1])


if __name__ == '__main__':
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    assert rect.perimeter() == 23.52
    
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    assert rect.area() == 32.14
