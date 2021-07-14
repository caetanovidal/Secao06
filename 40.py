n = int(input("informe um numero: "))
maior = -999
menor = 999
limbo = 0
while n > 0:
    n = int(input("informe um numero: "))
    if n > maior:
        maior = n
    if n < 0:
        limbo = n
    elif n < menor:
        menor = n
print(f'maior numero digitado = {maior}')
print(f'menor numero digitado = {menor}')
