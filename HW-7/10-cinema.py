G = int(input("Введите число девочек: "))
B = int(input("Введите число мальчиков: "))
ansB, ansG = "B", "G"
cntG, cntB = 2, 1
dif = abs(B-G)
steps = B + G - dif
if B < G: ansB,ansG = ansG,ansB
if B > 2*G: print("Нет решения")
else:
    for i in range(1, steps//2 + 1):
        print(ansB, end='')
        print(ansG, end='')
        if dif > 0:
            print(ansB, end = '')
            dif -= 1