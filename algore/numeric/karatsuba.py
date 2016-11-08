

from math import floor, ceil


def karatsuba(x, y):
    n = max(len(bin(x)), len(bin(y))) - 2
    if n <= 32:
        return x * y
    bx = bin(x).replace('0b', '')
    by = bin(y).replace('0b', '')
    while len(bx) is not len(by):
        if len(bx) is not n:
            bx = '0{0}'.format(bx)
        elif len(by) is not n:
            by = '0{0}'.format(by)
    xh = int(bx[:floor(n/2)], 2)
    xl = int(bx[ceil(n/2):], 2)
    yh = int(by[:floor(n/2)], 2)
    yl = int(by[ceil(n/2):], 2)
    p = karatsuba(xh, yh)
    q = karatsuba(xl, yl)
    r = karatsuba(xh+xl, yh+yl)
    return (p << (2 * ceil(n/2))) + ((r - p - q) << ceil(n/2)) + q
