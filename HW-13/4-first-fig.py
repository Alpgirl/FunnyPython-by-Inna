num = float(input('Введите положительное действительное число: '))

res = round(round(num - int(num), 1) * 10)
print("Первая цифра после десятичной точки:", res)
