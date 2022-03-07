x = float(input("Введите значение переменной x: "))
res = 1
error = False
for i in range(1, 9):
    if x == 2**i:
        print("Ошибка")
        error = True
        break
    res *= (x - 2**i - 1)/(x - 2**i)
if not error: print(x)