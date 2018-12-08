from fraction import Fraction
from random import randint
from sys import argv
def decrypt(x, y, p, k):
    a = (y - k) / (x - p)
    b = y - x*a
    r = x*x + y*y
    m = (b*b - r) / ((a*a + Fraction(1))*x)
    e = a*m + b
    return e

def encrypt(m, e, p, k):
    a = (e - k) / (m - p)
    b = e - m*a
    r = m*m + e*e
    x = (b*b - r) / ((a*a + Fraction(1))*m)
    y = a*x + b
    return (x,y)

mode = argv[1]
if mode == '-h':
    print("python3 sdmppo.py [-e/-d] m e p k")
args = [argv[x].split('/') for x in range(2,6)]
for i in range(0, len(args)):
    arg = args[i]
    if len(arg) == 1:
        args[i] = Fraction(int(arg[0]))
    elif len(arg) == 2:
        args[i] = Fraction(int(arg[0]), int(arg[1]))
    else:
        print("Konstrukcja argumentów powinna być taka: a/b albo a jeśli b = 1.")
        exit()
if mode == '-e':
    C = encrypt(args[0], args[1], args[2], args[3])
    print("x = {}".format(C[0]))
    print("y = {}".format(C[1]))

elif mode == '-d':
    print("e = {}".format(decrypt(args[0], args[1], args[2], args[3])))
