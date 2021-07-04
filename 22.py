qtd = 0
soma = 0
print("informe nota entre 10 e 20\ninforme algum numero fora desses para receber média")
nota = int(input("informe a nota1: "))

while 10 <= nota <= 20:
    qtd = qtd + 1
    soma = soma + nota
    nota = int(input(f'informe a nota{qtd + 1}: '))

media = soma/qtd
print(media)

