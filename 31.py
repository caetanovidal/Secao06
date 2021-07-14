s = 0
cima = 1
baixo = 1
for i in range(1, 51):
    s = s + (cima / baixo)
    cima = cima + 2
    baixo = baixo + 1

print(s)

'''
OUTRA FORMA: 

denominador = 0
resultado = 0

for n in range(1, 101, 2):
    denominador += 1
    divisao = n / denominador
    resultado += divisao

    print(f'{n}/{denominador}', )
print(f'A soma de todos os termos anteriores é igual a {resultado:.2f}')'''

