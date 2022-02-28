cur_sum = int(input("Введите текущую сумму вклада, руб: "))
percent = float(input("Введите процентую ставку, %: "))
res_sum = int(input("Введите итоговую сумму: "))

year = 0
while (cur_sum < res_sum):
    cur_sum += int(cur_sum * percent / 100)
    year += 1
    print(cur_sum)
print(year)
