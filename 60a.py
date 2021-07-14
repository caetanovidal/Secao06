n = int(input("informe um numero: "))
lista = []
pares = []
while n != 0:
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    n = int(input("informe um numero: "))

print(f'soma = {sum(lista)}')
print(f'maior numero = {max(lista)}')
print(f'menor numero = {min(lista)}')
print(f'tamanho = {len(lista)}')
print(f'média = {sum(lista) / len(lista)}')
print(f'soma dos pares = {sum(pares)}')
print(f'média dos pares = {sum(pares) / len(pares)}')
