num = int(input("informe um numero: "))
while num < 0 or num % 2 != 0:
    print("informe numero positivo e par!")
    num = int(input("informe um numero: "))
for i in range(num, -1, -1):
    if i % 2 == 0:
        print(i)
