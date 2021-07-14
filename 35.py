entrada = int(input("informe um valor inicial: "))
saida = int(input("informe um valor final: "))
soma =0
while saida < entrada:
    print("intervalo invalido!")
    entrada = int(input("informe um valor inicial: "))
    saida = int(input("informe um valor final: "))

for i in range(entrada, saida + 1):
    if i % 2 != 0:
        soma = soma + i
print(f'soma dos impares neste intervalo = {soma}')