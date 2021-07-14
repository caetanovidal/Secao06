n = int(input("informe um numero: "))

if n == 1:
    print("numero nao é primo")
if n == 2:
    print("numero primo!")
elif n == 3:
    print("numero primo!")
elif n == 5:
    print("numero primo!")
elif n == 7:
    print("numero primo!")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("nao é primo")
else:
    print("numero primo!")

