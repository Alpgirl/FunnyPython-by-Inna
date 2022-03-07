length = float(input("Введите длину письма: "))
cnt = 0
while length >= 12:
    length /= 2
    cnt += 2
print(cnt)
