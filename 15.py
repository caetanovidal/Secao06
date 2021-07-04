num = int(input("informe um numero: "))
while num < 0 or num % 2 ==0:
    print("informe um numero positivo e impar!")
    num = int(input("informe um numero: "))
for i in range(0, num + 1):
    if i % 2 != 0:
        print(i)
