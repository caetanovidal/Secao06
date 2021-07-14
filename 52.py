saque = int(input("informe o valor do saque: "))

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
while True:
    if saque - 100 >= 0:
        saque = saque - 100
        cem += 1
    elif saque - 50 >= 0:
        saque = saque - 50
        cinquenta += 1
    elif saque - 20 >= 0:
        saque = saque - 20
        vinte += 1
    elif saque - 10 >= 0:
        saque = saque - 10
        dez += 1
    elif saque - 5 >= 0:
        saque = saque - 5
        cinco += 1
    elif saque - 2 >= 0:
        saque = saque - 2
        dois += 1
    elif saque - 1 >= 0:
        saque = saque - 1
        um += 1
    if saque == 0:
        break

print(f'Serão utilizdas {cem} notas de 100, {cinquenta} notas de 50, {vinte} notas de 20, {dez} notas de 10, {cinco} '
      f'notas de 5, {dois} notas de 2, e {um} notas de 1')
