# Дроби v0.2
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
# Предусмотрите возможность задать отрицательные числитель и/или знаменатель.
# А также перепишите методы __str__ и __repr__ таким образом, чтобы информация
# об объекте согласовывалась с инициализацией строкой.
# Далее реализуйте оператор математического отрицания — унарный минус.
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с
# использованием ведущих символов нижнего подчёркивания).
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# a = Fraction(1, 3)
# b = Fraction(-2, -6)
# c = Fraction(-3, 9)
# d = Fraction(4, -12)
# print(a, b, c, d)
# print(*map(repr, (a, b, c, d)))
# Вывод
# 1/3 1/3 -1/3 -1/3
# Fraction('1/3') Fraction('1/3') Fraction('-1/3') Fraction('-1/3')
# Пример 2
# Ввод
# a = Fraction('-1/2')
# b = -a
# print(a, b, a is b)
# b.numerator(-b.numerator())
# a.denominator(-3)
# print(a, b)
# print(a.numerator(), a.denominator())
# print(b.numerator(), b.denominator())
# Вывод
# -1/2 1/2 False
# 1/3 -1/2
# 1 3
# 1 2

class Fraction():

    def __init__(self, num=1, denom=1):
        from math import gcd
        if isinstance(num, str):
            num, denom = map(int, num.split('/'))
        if denom < 0:
            num, denom = -num, -denom
        n = gcd(num, denom)
        self.num, self.denom = num // n, denom // n

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
    b = Fraction(-2, -6)
    c = Fraction(-3, 9)
    d = Fraction(4, -12)
    print(a, b, c, d)
    print(*map(repr, (a, b, c, d)))

    a = Fraction('-1/2')
    b = -a
    print(a, b, a is b)
    b.numerator(-b.numerator())
    a.denominator(-3)
    print(a, b)
    print(a.numerator(), a.denominator())
    print(b.numerator(), b.denominator())

    a = Fraction(1, -33)
    print(a)
    print(a.numerator(-3), a)
    print(a.numerator(), a.denominator())
