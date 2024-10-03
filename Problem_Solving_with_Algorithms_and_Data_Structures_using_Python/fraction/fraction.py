
def gcd(m, n):

    while m % n != 0:
        m, n = n, m % n

    return n

class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):

        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other):

        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):

        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):

        return self.num * other.den == other.num * self.den

    def __lt__(self, other):

        return self.num * other.den < other.num * self.den
    
    def __gt__(self, other):

        return self.num * other.den > other.num * self.den



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

main()
