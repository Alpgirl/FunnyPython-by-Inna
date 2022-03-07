N = int(input("Введите число N: "))
s = 1
for num in range(1, N + 1):
    s += float((-1)**num * 2**(-num))
print(s)
