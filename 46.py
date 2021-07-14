import random

# x = 500
x = random.randint(1, 1000)
qtd = 1
n = int(input("O computador gerou um numero entre 1 e 1000, tente acertar: "))
while True:
    if n < x:
        print("informe um numero maior!")
    if n > x:
        print("informe um numero menor!")
    if n == x:
        print("parabens voce acertou!!!")
        break
    qtd += 1
    n = int(input("O computador gerou um numero entre 1 e 1000, tente acertar: "))
print(f'tentativas = {qtd}')
