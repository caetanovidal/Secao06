n = 11
soma = 0
soma2 = 0
soma3 = 0
for i in range(1, n+1):
    soma = soma + i


for i in range(1, (n*2)):
    if i % 2 != 0:
        soma3 = soma3 + i

print(soma)
print(soma3)
