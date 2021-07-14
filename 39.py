b = int(input("informe a base: "))
h = int(input("informe a altura: "))
while h <= 0 or b <= 0:
    print('numeros invalidos')
    b = int(input("informe a base: "))
    h = int(input("informe a altura: "))

area = b*h/2
print(f'area do triangulo = {area}')
