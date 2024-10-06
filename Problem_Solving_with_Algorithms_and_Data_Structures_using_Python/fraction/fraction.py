
def gcd(m, n):

    while m % n != 0:
        m, n = n, m % n

    return n

class Fraction:

    def __init__(self, top, bottom):

        if not type(top) is int:
            raise RunTimeError(f"Error: top {top} not an integer.")
        if not type(bottom) is int:
            raise RunTimeError(f"Error: bottom {bottom} not an integer.")

        if bottom < 0:
            top, bottom = -top, -bottom
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def getNum(self):

        return self.num

    def getDen(self):

        return self.den

    def __str__(self):

        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):

        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):

        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):

        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):

        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self, other):

        return self.num * other.den == other.num * self.den

    def __lt__(self, other):

        return self.num * other.den < other.num * self.den

    def __le__(self, other):

        return self < other or self == other
    
    def __gt__(self, other):

        return self.num * other.den > other.num * self.den

    def __ge__(self, other):

        return self > other or self == other

    def __ne__(self, other):

        return not self == other



def main():
    fract = Fraction(3, 5)
    print(fract)
    print("I ate", fract, "of the pizza.")
    print(fract.__str__())
    print(str(fract))
    print()

    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)

    f3 = f1 + f2
    print(f"{f1} + {f2} = {f3}")
    print()

    f4 = f1 - f2
    print(f"{f1} - {f2} = {f4}")
    print()

    print(f"gcd(20, 10) == {gcd(20, 10)}")
    print()

    
    print(f"{f1} == {f2} is {f1 == f2}")
    f1 = Fraction(1, 4)
    f2 = Fraction(64, 256)
    print(f"{f1} == {f2} is {f1 == f2}")
    print()

    f1 = Fraction(5, 6)
    f2 = Fraction(4, 15)
    f3 = f1 * f2
    print(f"{f1} * {f2} = {f3}")
    print()

    f1 = Fraction(5, 6)
    f2 = Fraction(4, 15)
    f3 = f1 / f2
    print(f"{f1} / {f2} = {f3}")
    print()

    f1 = Fraction(1, 4)
    f2 = Fraction(2, 3)
    print(f"{f1} < {f2} is {f1 < f2}")
    print(f"{f2} < {f1} is {f2 < f1}")
    print(f"{f1} > {f2} is {f1 > f2}")
    print(f"{f2} > {f1} is {f2 > f1}")
    print()

    f = Fraction(2, 4)
    print(f"num is {f.getNum()} and den is {f.getDen()}")
    print()

    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    f3 = f1 + f2
    print(f"{f1} + {f2} = {f3}")
    print()

    f1 = Fraction(1, 2)
    f2 = Fraction(3, 6)
    f3 = Fraction(2, 3)
    print(f"{f1} <= {f2} is {f1 <= f2}")
    print(f"{f1} <= {f3} is {f1 <= f3}")
    print(f"{f3} <= {f1} is {f3 <= f1}")
    print()

    f1 = Fraction(1, 2)
    f2 = Fraction(3, 6)
    f3 = Fraction(2, 3)
    print(f"{f1} >= {f2} is {f1 >= f2}")
    print(f"{f1} >= {f3} is {f1 >= f3}")
    print(f"{f3} >= {f1} is {f3 >= f1}")
    print()

    f1 = Fraction(1, 2)
    f2 = Fraction(3, 6)
    f3 = Fraction(2, 3)
    print(f"{f1} != {f2} is {f1 != f2}")
    print(f"{f1} != {f3} is {f1 != f3}")
    print(f"{f3} != {f1} is {f3 != f1}")
    print()

    try:
        f = Fraction(12.3, 4)
    except:
        print("Ok")
    try:
        f = Fraction(12, 4.2)
    except:
        print("Ok")
    print()

    f = Fraction(2, -10)
    print(f)
    print()

main()
