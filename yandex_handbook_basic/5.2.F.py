# Дроби v0.3
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
# Реализуйте бинарные операторы:
#     + — сложение дробей, создаёт новую дробь;
#     - — вычитание дробей, создаёт новую дробь;
#     += — сложение дробей, изменяет дробь, переданную слева;
#     -= — вычитание дробей, изменяет дробь, переданную слева.
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть
# с использованием ведущих символов нижнего подчёркивания).
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# a = Fraction(1, 3)
# b = Fraction(1, 2)
# c = a + b
# print(a, b, c, a is c, b is c)
# Вывод
# 1/3 1/2 5/6 False False
# Пример 2
# Ввод
# a = Fraction(1, 8)
# c = b = Fraction(3, 8)
# b -= a
# print(a, b, c, b is c)
# Вывод
# 1/8 1/4 1/4 True

class Fraction():

    def __init__(self, num=1, denom=1):
        from math import gcd
        if isinstance(num, str):
            num, denom = map(int, num.split('/'))
        if denom < 0:
            num, denom = -num, -denom
        n = gcd(num, denom)
        self.num, self.denom = num // n, denom // n

    def __add__(self, other):
        num = self.num * other.denom + other.num * self.denom
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __iadd__(self, other):
        from math import gcd
        num = self.num * other.denom + other.num * self.denom
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __sub__(self, other):
        num = self.num * other.denom - other.num * self.denom
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __isub__(self, other):
        from math import gcd
        num = self.num * other.denom - other.num * self.denom
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __str__(self):
        return F"{self.num}/{self.denom}"

    def __repr__(self):
        return F"Fraction('{self.num}/{self.denom}')"

    def __neg__(self):
        return self.__class__(-self.num, self.denom)

    def numerator(self, num=None):
        from math import gcd
        if num is None:
            return abs(self.num)

        sign = -1 if self.num < 0 else 1
        num *= sign

        n = gcd(num, self.denom)
        self.num = num // n
        self.denom //= n
        return abs(self.num)

    def denominator(self, denom=None):
        from math import gcd
        if denom is None:
            return self.denom

        if denom < 0:
            self.num, denom = -self.num, -denom
        n = gcd(self.num, denom)
        self.num //= n
        self.denom = denom // n
        return self.denom


if __name__ == '__main__':
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    c = a + b
    print(a, b, c, a is c, b is c)

    a = Fraction(1, 8)
    c = b = Fraction(3, 8)
    b -= a
    print(a, b, c, b is c)

