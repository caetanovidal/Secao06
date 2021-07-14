n = int(input("informe um numero: "))
tot = 0

for c in range(2, n + 1):
    if n % c == 0:
        tot += 1
if tot == 1:
    print("numero primo!")
else:
    print("numero nao é primo")
