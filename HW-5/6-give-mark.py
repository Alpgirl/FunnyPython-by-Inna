num, pos, neg = 1, 0, 0
while (num != 0):
    num = int(input("Введите число: "))
    if num > 0: pos += 1
    elif num < 0: neg += 1
print("Кол-во положительных чисел: ", pos)
print("Кол-во отрицательных чисел: ", neg)
