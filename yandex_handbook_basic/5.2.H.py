# Дроби v0.5
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Следующим этапом разработки будет реализация методов сравнения:
# >, <, >=, <=, ==, !=.
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
# print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
# Вывод
# False True False True False False
# Пример 2
# Ввод
# a = Fraction(1, 3)
# b = Fraction(6, 2).reverse()
# print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
# Вывод
# False False True True True True

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

    def __mul__(self, other):
        num = self.num * other.num
        denom = self.denom * other.denom
        return self.__class__(num, denom)

    def __imul__(self, other):
        from math import gcd
        num = self.num * other.num
        denom = self.denom * other.denom
        n = gcd(num, denom)
        self.num = num // n
        self.denom = denom // n
        return self

    def __truediv__(self, other):
        num = self.num * other.denom
        denom = self.denom * other.num
        return self.__class__(num, denom)

    def __itruediv__(self, other):
        from math import gcd
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
        return self.num * other.denom < other.num * self.denom

    def __eq__(self, other):
        return self.num == other.num and self.denom == other.denom

    def __le__(self, other):
        return self.num * other.denom <= other.num * self.denom

    def __neq__(self, other):
        return self.num != other.num or self.denom != other.denom

    def __gt__(self, other):
        return self.num * other.denom > other.num * self.denom

    def __ge__(self, other):
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
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    print(a > b, a < b, a >= b, a <= b, a == b, a >= b)

    a = Fraction(1, 3)
    b = Fraction(6, 2).reverse()
    print(a > b, a < b, a >= b, a <= b, a == b, a >= b)

