n = int(input("informe um numero: "))
soma = 0
qtd = 0

maior = -999
menor = 999
somap = 0
mediap = 0
qtdp = 0
while n != 0:
    soma = soma + n
    qtd = qtd + 1
    if n > maior:
        maior = n
    if n  < menor:
        menor = n
    if n % 2 == 0:
        qtdp = qtdp + 1
        somap = somap + n

    n = int(input("informe um numero: "))

media = soma/qtd
mediap = somap/qtdp

print(f'soma total = {soma}')
print(f'quantidade total = {qtd}')
print(f'média total = {media}')
print(f'maior numero = {maior}')
print(f'menor numero = {menor}')
print(f'soma dos pares = {somap}')
print(f'media dos pares = {mediap}')
