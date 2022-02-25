num1 = float(input("Введите 1-е число: "))
num2 = float(input("Введите 2-е число: "))
num3 = float(input("Введите 3-е число: "))

max = num1
if num2 >= max:
    max = num2
if num3 >= max:
    max = num3

print("Максимальное число: ", max)