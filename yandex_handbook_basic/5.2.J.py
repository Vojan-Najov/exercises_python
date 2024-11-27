# Дроби v0.7
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# "Остался последний штрих!" Правда звучит как издевательство?
# Мы «научили» наши дроби работать с целыми числами и вот теперь надо
# провернуть обратное действие. Реализуйте функционал, который позволит
# производить все арифметические операции с дробями и числами, независимо от их
# положения (слева или справа) в операторе.
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с
# использованием ведущих символов нижнего подчёркивания).
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# a = Fraction(1)
# b = Fraction('2')
# c, d = map(Fraction.reverse, (2 + a, -1 + b))
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
# c, d = map(Fraction.reverse, (3 - a, 2 / b))
# print(a, b, c, d)
# print(a > b, c > d)
# print(a >= 1, b >= 1, c >= 1, d >= 1)
# Вывод
# 1/2 2/3 2/5 1/3
# False True
# False False False False

class Fraction():

    def __init__(self, num=1, denom=1):
        from math import gcd
        if isinstance(num, str):
            if num.isnumeric():
                num, denom = int(num), 1
            else:
                num, denom = map(int, num.split('/'))
        if denom < 0:
            num, denom = -num, -denom
        n = gcd(num, denom)
        self.num, self.denom = num // n, denom // n

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return self.__add__(Fraction(other))

        num = self.num * other.denom + other.num * self.denom
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __radd__(self, other):
        return self.__add__(Fraction(other))

    def __iadd__(self, other):
        from math import gcd

        if not isinstance(other, self.__class__):
            return self.__iadd__(Fraction(other))

        num = self.num * other.denom + other.num * self.denom
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return self.__sub__(Fraction(other))

        num = self.num * other.denom - other.num * self.denom
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __rsub__(self, other):
        return Fraction(other).__sub__(self)

    def __isub__(self, other):
        from math import gcd

        if not isinstance(other, self.__class__):
            return self.__isub__(Fraction(other))

        num = self.num * other.denom - other.num * self.denom
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            return self.__mul__(Fraction(other))

        num = self.num * other.num
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __rmul__(self, other):
        return self.__mul__(Fraction(other))

    def __imul__(self, other):
        from math import gcd

        if not isinstance(other, self.__class__):
            return self.__imul__(Fraction(other))

        num = self.num * other.num
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __truediv__(self, other):
        if not isinstance(other, self.__class__):
            return self.__truediv__(Fraction(other))

        num = self.num * other.denom
        denom = self.denom * other.num
        return self.__class__(num, denom)

    def __rtruediv__(self, other):
        return Fraction(other).__truediv__(self)

    def __itruediv__(self, other):
        from math import gcd

        if not isinstance(other, self.__class__):
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
        if not isinstance(other, self.__class__):
            return self.__lt__(Fraction(other))

        return self.num * other.denom < other.num * self.denom

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return self.__eq__(Fraction(other))

        return self.num == other.num and self.denom == other.denom

    def __le__(self, other):
        if not isinstance(other, self.__class__):
            return self.__le__(Fraction(other))

        return self.num * other.denom <= other.num * self.denom

    def __neq__(self, other):
        if not isinstance(other, self.__class__):
            return self.__neq__(Fraction(other))

        return self.num != other.num or self.denom != other.denom

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return self.__gt__(Fraction(other))

        return self.num * other.denom > other.num * self.denom

    def __ge__(self, other):
        if not isinstance(other, self.__class__):
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
    c, d = map(Fraction.reverse, (2 + a, -1 + b))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)

    print()

    a = Fraction(1, 2)
    b = Fraction('2/3')
    c, d = map(Fraction.reverse, (3 - a, 2 / b))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)

    print()
    print(1 + Fraction(1, 3))
    print(1 - Fraction(1, 3))
    print(1 * Fraction(1, 3))
    print(1 / Fraction(1, 3))
    print(1 < Fraction(1, 3))
    print(1 <= Fraction(1, 3))
    print(1 > Fraction(1, 3))
    print(1 >= Fraction(1, 3))
    print(1 == Fraction(1, 3))
    print(1 != Fraction(1, 3))

    print()
    print(-2 + Fraction(1, 3))
    print(-2 - Fraction(1, 3))
    print(-2 * Fraction(1, 3))
    print(-2 / Fraction(1, 3))
    print(-2 < Fraction(1, 3))
    print(-2 <= Fraction(1, 3))
    print(-2 > Fraction(1, 3))
    print(-2 >= Fraction(1, 3))
    print(-2 == Fraction(1, 3))
    print(-2 != Fraction(1, 3))

    print()
    print(1 + -Fraction(1, 3))
    print(1 - -Fraction(1, 3))
    print(1 * -Fraction(1, 3))
    print(1 / -Fraction(1, 3))
    print(1 < -Fraction(1, 3))
    print(1 <= -Fraction(1, 3))
    print(1 > -Fraction(1, 3))
    print(1 >= -Fraction(1, 3))
    print(1 == -Fraction(1, 3))
    print(1 != -Fraction(1, 3))

    print()
    print(0 + -Fraction(1, 3))
    print(0 - -Fraction(1, 3))
    print(0 * -Fraction(1, 3))
    print(0 / -Fraction(1, 3))
