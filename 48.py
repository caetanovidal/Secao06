x1 = 0
x2 = 1

soma = 0
while True:
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    print(x3)
    if x3 > 4_000_000:
        break
    elif x3 % 2 == 0 and x3 < 4_000_000 and soma < 4_000_000:
        soma = soma + x3
print(soma)

