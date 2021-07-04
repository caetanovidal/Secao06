qtd = int(input("informe a quantidade de numeros: "))
while qtd <= 0:
    print("quantaidade deve ser positiva!")
    qtd = int(input("informe a quantidade de numeros: "))
maior = -999
contador = 0
for i in range(0, qtd):
    num = int(input("informe um numero: "))
    if num > maior:
        maior = num
        contador = contador + 1
print(f'maior numero = {maior}')
print(f'quantidade de vezes em que o numero maior foi trocado = {contador}')
