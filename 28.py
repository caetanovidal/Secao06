import math

n = int(input("informe um numero: "))
constante = 1
soma = 0
for i in range(1, n+1):
    soma = soma + (constante/(math.factorial(int(i))))
print(soma)
