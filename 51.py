x = 1.5
aumento = 2000/100 * x
salario = 2000 + aumento
ano = 1997

while True:
    x = x * 2
    aumento = 2000/100 * x
    salario = 2000 + aumento
    ano += 1
    if ano == 2021:
        break
print("salario = {0:.2f}".format(salario))
