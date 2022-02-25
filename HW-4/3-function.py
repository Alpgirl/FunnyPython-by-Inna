x = float(input("Введите икс: "))

if x < 0:
    y = x**2
elif x == 0:
    y = 5
else:
    y = x - 12

print("Игрек равен: ", y)