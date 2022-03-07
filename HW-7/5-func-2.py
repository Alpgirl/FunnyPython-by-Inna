start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
c = int(input("Введите число шаг: "))

for x in range(end, start - 1, c):
    print("В точке", x, "ф-ция равна ", x**3 + x**2 * 2 - 4 * x + 1)