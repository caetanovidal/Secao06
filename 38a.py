for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        d = a + b + c
        if (a*a) + (b*b) == (c*c):
            print(a, b, c, d)
