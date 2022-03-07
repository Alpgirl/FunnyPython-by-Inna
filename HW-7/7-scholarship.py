grant = float(input("Введите стипендию: "))
expenses = float(input("Введите расходы на проживание: "))
sum = expenses - grant
for month in range(1, 10):
    expenses += expenses * 0.03
    sum += expenses - grant
print("У родителей необходимо попросить: ", round(sum, 3))

