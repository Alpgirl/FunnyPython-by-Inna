average = 0
for cnt in range(1, 13):
    print("Введите зарплату за ", cnt, "-й месяц: ", end = "", sep = "")
    salary_per_month = int(input())
    average += salary_per_month
print("Среднегодовая зарплата сотрудника: ", round(average/12, 2))