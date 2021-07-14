carlos = 3000
joao = 1000
meses = 0

renda1 = carlos/100 * 2
total1 = renda1 + carlos

while True:
    renda1 = carlos/100 * 2
    total1 = renda1 + carlos
    carlos = total1

    renda2 = joao/100 * 5
    total2 = renda2 + joao
    joao = total2

    meses = meses + 1
    if total2 >= total1:
        break
print('total acumulado por carlos em {0} meses foi de {1:.2f} reais'.format(meses, total1))
print('total acumulado por joao em {0} meses foi de {1:.2f} reais'.format(meses, total2))
