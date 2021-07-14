stop = int(input("informe um numero: "))
contador = 0
n = 1
soma = 0
tot = 0
nao_primos = []
while True:
    for i in range(1, n + 1):
        if n % i == 0:
            tot += 1
    if tot == 2:
        soma = soma + n
        contador = contador + 1
    if contador == stop:
        break
    else:
        n += 1
        tot = 0
print(soma)

