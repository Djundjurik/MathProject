from math import *


func = str(input())


def f(x):
    return eval(func)


def rect(a, b, m):
    h = (b - a) / m
    s = sum(f((2 * m - 1) * h / 2) for m in range(1, m + 1))
    return s * (b - a) / m


def trapez(a, b, m):
    h = (b - a) / m
    s = f(a) + f(b) + 2*sum(f(a+m*h) for m in range(1, m))
    return s * h / 2


def simp(a, b, m):
    h = (b - a) / m
    s = f(a) + f(b)
    pogr = 10**-10

    for m in range(1, m):
        try:
            s += (2 + 2*(m % 2))*f(a+m*h)
        finally:
            s += (2 + 2*(m % 2))*f(a+m*h)
    return s*h/3

print(simp(-1, 1,100000))
