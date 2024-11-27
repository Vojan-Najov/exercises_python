# Дроби v0.6
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Надо было, наверное, раньше об этом подумать...
# Эти слова так и срываются с языка при разработке какого либо программного обеспечения.
# Все же понимают, что целые числа тоже являются дробями?! Следовательно, нам
# требуется изменить систему инициализации, чтобы она могла воспринимать и
# целые числа (причём и в виде строк). Ну и естественно, требуется переработать
# операторы арифметических действий и сравнения.
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть
# с использованием ведущих символов нижнего подчёркивания).
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# a = Fraction(1)
# b = Fraction('2')
# c, d = map(Fraction.reverse, (a + 2, b - 1))
# print(a, b, c, d)
# print(a > b, c > d)
# print(a >= 1, b >= 1, c >= 1, d >= 1)
# Вывод
# 1/1 2/1 1/3 1/1
# False False
# True True False True
# Пример 2
# Ввод
# a = Fraction(1, 2)
# b = Fraction('2/3')
# c, d = map(Fraction.reverse, (a + 2, b - 1))
# print(a, b, c, d)
# print(a > b, c > d)
# print(a >= 1, b >= 1, c >= 1, d >= 1)
# Вывод
# 1/2 2/3 2/5 -3/1
# False True
# False False False False

class Fraction():

    def __init__(self, num=1, denom=1):
        from math import gcd
        if isinstance(num, str):
            if num.isnumeric():
                num, denum = int(num), 1
            else:
                num, denom = map(int, num.split('/'))
        if denom < 0:
            num, denom = -num, -denom
        n = gcd(num, denom)
        self.num, self.denom = num // n, denom // n

    def __add__(self, other):
        if isinstance(other, int):
            return self.__add__(Fraction(other))

        num = self.num * other.denom + other.num * self.denom
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __radd__(self, other):
        return self.__add__(Fraction(other))

    def __iadd__(self, other):
        from math import gcd

        if isinstance(other, int):
            return self.__iadd__(Fraction(other))

        num = self.num * other.denom + other.num * self.denom
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            return self.__sub__(Fraction(other))

        num = self.num * other.denom - other.num * self.denom
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __isub__(self, other):
        from math import gcd

        if isinstance(other, int):
            return self.__isub__(Fraction(other))

        num = self.num * other.denom - other.num * self.denom
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__mul__(Fraction(other))

        num = self.num * other.num
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __imul__(self, other):
        from math import gcd

        if isinstance(other, int):
            return self.__imul__(Fraction(other))

        num = self.num * other.num
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __truediv__(self, other):
        if isinstance(other, int):
            return self.__truediv__(Fraction(other))

        num = self.num * other.denom
        denom = self.denom * other.num
        return self.__class__(num, denom)

    def __itruediv__(self, other):
        from math import gcd

        if isinstance(other, int):
            return self.__itruediv__(Fraction(other))

        num = self.num * other.denom
        denom = self.denom * other.num
        if denom < 0:
            num, denom = -num, -denom
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

    def __lt__(self, other):
        if isinstance(other, int):
            return self.__lt__(Fraction(other))

        return self.num * other.denom < other.num * self.denom

    def __eq__(self, other):
        if isinstance(other, int):
            return self.__eq__(Fraction(other))

        return self.num == other.num and self.denom == other.denom

    def __le__(self, other):
        if isinstance(other, int):
            return self.__le__(Fraction(other))

        return self.num * other.denom <= other.num * self.denom

    def __neq__(self, other):
        if isinstance(other, int):
            return self.__neq__(Fraction(other))

        return self.num != other.num or self.denom != other.denom

    def __gt__(self, other):
        if isinstance(other, int):
            return self.__gt__(Fraction(other))

        return self.num * other.denom > other.num * self.denom

    def __ge__(self, other):
        if isinstance(other, int):
            return self.__ge__(Fraction(other))

        return self.num * other.denom >= other.num * self.denom

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

    def reverse(self):
        return self.__class__(self.denom, self.num)


if __name__ == '__main__':
    a = Fraction(1)
    b = Fraction('2')
    c, d = map(Fraction.reverse, (a + 2, b - 1))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)

    a = Fraction(1, 2)
    b = Fraction('2/3')
    c, d = map(Fraction.reverse, (a + 2, b - 1))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)

