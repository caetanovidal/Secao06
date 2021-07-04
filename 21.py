n = int(input("informe um numero: "))
n1 = int(input("informe um numero: "))
soma = 0
multiplicacao = 1
for i in range(n, n1+1):
    if i % 2 == 0:
        soma = soma + i
    else:
        multiplicacao = multiplicacao * i
print(soma)
print(multiplicacao)
