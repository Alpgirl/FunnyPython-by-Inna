start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
c = int(input("Введите число c: "))

s,n = 0,0
for num in range(start, end + 1):
    if num % c == 0:
        s += num
        n += 1

print("Среднее арифметическое чисел, кратных ", c, ", = ", s/n)