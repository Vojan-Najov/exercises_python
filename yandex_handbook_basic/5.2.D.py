# Дроби v0.1
# Ограничение времени
# 1 с
# Ограничение памяти
# 64.0 Мб
# Ввод
# стандартный ввод
# Вывод
# стандартный вывод
# Возможно, вы уже заметили, что дробные числа (float) недостаточно точные для
# некоторых задач. Для более точных математических расчётов иногда прибегают к
# созданию правильных рациональных дробей, описываемых числителем и знаменателем.
# Начнём разработку класса Fraction, который реализует предлагаемые дроби.
# Предусмотрите возможность инициализации дроби с помощью двух целых чисел или
# строки в формате <числитель>/<знаменатель>.
# В случаях наличия общего делителя у числителя и знаменателя, дробь следует
# сократить.
# А также реализуйте методы:
#     numerator() — возвращает значение числителя;
#     numerator(number) — изменяет значение числителя и производит сокращение
#                         дроби, если это необходимо;
#     denominator() – возвращает значение знаменателя;
#     denominator(number) — изменяет значение знаменателя и производит
#                           сокращение дроби, если необходимо;
#     __str__ — возвращает строковое представление дроби в формате
#               <числитель>/<знаменатель>;
#     __repr__ — возвращает описание объекта в формате
#                Fraction(<числитель>, <знаменатель>).
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все числа в данной задаче будут положительными.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть
# с использованием ведущих символов нижнего подчёркивания).
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
# Пример 1
# Ввод
# fraction = Fraction(3, 9)
# print(fraction, repr(fraction))
# fraction = Fraction('7/14')
# print(fraction, repr(fraction))
# Вывод
# 1/3 Fraction(1, 3)
# 1/2 Fraction(1, 2)
# Пример 2
# Ввод
# fraction = Fraction(3, 210)
# print(fraction, repr(fraction))
# fraction.numerator(10)
# print(fraction.numerator(), fraction.denominator())
# fraction.denominator(2)
# print(fraction.numerator(), fraction.denominator())
# Вывод
# 1/70 Fraction(1, 70)
# 1 7
# 1 2

class Fraction():

    def __init__(self, num=1, denom=1):
        from math import gcd
        if isinstance(num, str):
            num, denom = map(int, num.split('/'))
        n = gcd(num, denom)
        self.num, self.denom = num // n, denom // n

    def __str__(self):
        return F"{self.num}/{self.denom}"

    def __repr__(self):
        return F"Fraction({self.num}, {self.denom})"

    def numerator(self, num=None):
        from math import gcd
        if num is None:
            return self.num

        n = gcd(num, self.denom)
        self.num = num // n
        self.denom //= n

    def denominator(self, denom=None):
        from math import gcd
        if denom is None:
            return self.denom

        n = gcd(self.num, denom)
        self.num //= n
        self.denom = denom // n


if __name__ == '__main__':
    fraction = Fraction(3, 9)
    print(fraction, repr(fraction))
    fraction = Fraction('7/14')
    print(fraction, repr(fraction))

    fraction = Fraction(3, 210)
    print(fraction, repr(fraction))
    fraction.numerator(10)
    print(fraction.numerator(), fraction.denominator())
    fraction.denominator(2)
    print(fraction.numerator(), fraction.denominator())

