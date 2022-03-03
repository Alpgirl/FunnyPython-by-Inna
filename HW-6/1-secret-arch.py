input = "114 12 14 10605 4907 450"
table = input.split(" ")
for num in table:
    num = int(num)
    if num % 2 == 0 and num % 3  > 0:
        print(num, "Подходит")
    else:
        print(num, "Не подходит")