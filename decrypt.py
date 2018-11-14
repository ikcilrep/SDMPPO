
from random import randint
from decimal import Decimal


def sq(a):
    return a*a


def decrypt(c, p, k):
    m = c[0]
    e = c[1]
    p = Decimal(p)
    k = Decimal(k)
    a = (e - k) / (m - p)
    b = e - m * a
    r = sq(m) + sq(e)
    x = (sq(b) - r) / ((sq(a) + 1) * m)
    return round(x)

x = Decimal(input("Podaj wartość x:\t"))
y = Decimal(input("Podaj wartość y:\t"))
p = int(input("Podaj wartość p:\t"))
k = int(input("Podaj wartość k:\t"))

print("m = " + str(decrypt((x,y), p, k)))
