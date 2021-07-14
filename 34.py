from math import gcd

#comentado a forma que achei de fazer o codigo sem importar nada... e la embaixo usando o import math

n = 1
divisor = 1
'''while True:
    n = n + 1
    if n % 1 == 0 and n % 2 == 0 and n % 3 == 0 and n % 4 == 0 and n % 5 == 0 and n % 6 == 0 and n % 7 == 0 and n % 8 == 0 and n % 9 == 0 and n % 10 == 0:
        print(n)
        break'''

'''while True:
    n = n + 1
    if n % 1 == 0 and n % 2 == 0 and n % 3 == 0 and n % 4 == 0 and n % 5 == 0 and n % 6 == 0 and n % 7 == 0 and n % 8 == 0 and n % 9 == 0 and n % 10 == 0 and n % 11 == 0 and n % 12 == 0 and n % 13 == 0 and n % 14 == 0 and n % 15 == 0 and n % 16 == 0 and n % 17 == 0 and n % 18 == 0 and n % 19 == 0 and n % 20 == 0:
        print(n)
        break'''

'''while True:
    n = n + 1
    if n % 8 == 0 and n % 11 == 0 and n % 12 == 0 and n % 13 == 0 and n % 14 == 0 and n % 15 == 0 and n % 16 == 0 and n % 17 == 0 and n % 18 == 0 and n % 19 == 0 and n % 20 == 0:
        print(n)
        break'''


numeros = range(2, 21)


def mmc(numeros):
    m = 1
    for n in numeros:
        m = m * n // gcd(m, n)
    return m


print(mmc(numeros))


