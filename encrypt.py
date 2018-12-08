from random import randint
from fraction import Fraction



def encrypt(m, p, k):
    e = Fraction(randint(k.a, k.a << 10))
    a = (e - k) / (m - p)
    b = e - m*a
    r = m*m + e*e
    
    x = (b*b - r) / ((a*a + Fraction(1))*m)
    y = a*x + b
    return (x,y)

m = Fraction(int(input("Podaj wartość m:\t")))
p = Fraction(int(input("Podaj wartość p: ")))
k = Fraction(int(input("Podaj wartość k: ")))

C = encrypt(m, p, k)
print("x = {}".format(C[0]))
print("y = {}".format(C[1]))
