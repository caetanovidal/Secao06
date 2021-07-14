a = int(input("informe um numero: "))
b = int(input("informe um numero: "))
contador = 0
nao_primos = []
for n in range(a, b + 1):
    if n == 1:
        nao_primos.append(n)
    elif n == 2:
        contador += 1
    elif n == 3:
        contador += 1
    elif n == 5:
        contador += 1
    elif n == 7:
        contador += 1
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        nao_primos.append(n)
    else:
        contador += 1

print(contador)


