from random import randint
from fraction import Fraction


def decrypt(C, p, k):
    e = C[1]
    m = C[0]
    a = (e - k) / (m - p)
    b = e - m*a
    r = m*m + e*e
    x = (b*b - r) / ((a*a + Fraction(1))*m)
    y = a*x + b
    return x, y

x = input("Podaj wartość x: ")
y = input("Podaj wartość y: ")
p = Fraction(int(input("Podaj wartość p: ")))
k = Fraction(int(input("Podaj wartość k: ")))

x = x.split("/")
y = y.split("/")
x = Fraction(int(x[0]), int(x[1]))
y = Fraction(int(y[0]), int(y[1]))
m = decrypt((x , y), p, k)
print("m = {}".format(m[0]))
