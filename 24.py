n = int(input("informe um numero: "))
soma = 0
if n > 0:
    for i in range(1, n):
        if n % i == 0:
            soma = soma + i
if n < 0:
    for i in range(n+1, 0):
        if n % i == 0:
            soma = soma + i
print(soma)
