start_num = int(input("Введите начало отрезка: "))
end_num = int(input("Введите конец отрезка: "))
average,cnt = 0,0

for num in range(start_num, end_num + 1):
    if num % 3 == 0:
        average += num
        cnt += 1

print("Среднее арифметическое чисел, кратных 3 = ", average/cnt)

