from random import randint
from decimal import Decimal

def sq(a):
    return a*a


def encrypt(m, p, k):
    e = Decimal(randint(k << 20, k << 2048))
    m = Decimal(m)
    p = Decimal(p)
    k = Decimal(k)
    a = (e - k) / (m - p)
    b = e - m * a
    r = sq(m) + sq(e)
    x = (sq(b) - r) / ((sq(a) + 1) * m)
    y = a * x - b
    return (round(x), y)

m = Decimal(input("Podaj wartość m:\t"))
p = int(input("Podaj wartość p:\t"))
k = int(input("Podaj wartość k:\t"))
C = encrypt(m, p, k)
print("x = " + str(C[0]))
print("y = " + str(C[1]))
