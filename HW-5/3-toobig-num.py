sum = int(input("Введите сумму: "))
k = 0

if sum == 0: print(1)
else:
    while (sum != 0):
        sum //= 10
        k += 1
    print (k)
