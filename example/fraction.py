def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    # the methods go here
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        self.gcd = None

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_number = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        tmp = gcd(new_number, new_den)
        #common = gcd(new_number, new_den)
        return Fraction(new_number // tmp, new_number // tmp)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den

        return first_num == second_num

    def get_num(self):
        num = self.num
        return num

    def get_den(self):
        den = self.den
        return den


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)

num = Fraction.get_num(x)
den = Fraction.get_den(x)

print(num)
print(den)
