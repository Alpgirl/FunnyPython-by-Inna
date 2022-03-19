N = int(input("Введите длину списка: "))

resLst = [i % 5 if i % 2 != 0 else 1 for i in range(N)]
print("Результат:", resLst)

