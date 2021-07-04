n = int(input("informe um numero: "))
while n < 0:
    print("informe um numero positivo!")
    n = int(input("informe um numero: "))
soma = 0
for i in range(1, n+1):
    soma = soma + i
print(soma)
