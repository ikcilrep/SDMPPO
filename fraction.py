class Fraction:

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcf(self, a, b):
        return (a * b) // self.gcd(a, b)

    def shorten(self):
        gcd = self.gcd(self.a, self.b)
        if (self.a % gcd != 0) or (self.b % gcd != 0):
            print("GCD({}, {}) = {}".format(self.a, self.b, gcd))
        self.a //= gcd
        self.b //= gcd

        return self

    def extend_a(self, extend_to):
        return self.a * (extend_to // self.b)

    def __init__(self, a, b=1):
        self.a = a
        self.b = b
        self.shorten()

    def __add__(self, other):
        result_b = self.gcf(self.b, other.b)
        result_a = self.extend_a(result_b) + other.extend_a(result_b)
        return Fraction(result_a, result_b)

    def __mul__(self, other):
        result_a = self.a * other.a
        result_b = self.b * other.b
        return Fraction(result_a, result_b)

    def __sub__(self, other):
        return self + Fraction(-other.a, other.b)

    def __truediv__(self, other):
        return self * Fraction(other.b, other.a)

    def __str__(self):
        if self.b == 1:
            return str(self.a)
        return str(self.a)+"/"+str(self.b)
