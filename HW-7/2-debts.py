num_debtors = int(input('Введите количество должников: '))
s = 0

for choosed_debtor in range(0, num_debtors + 1, 5):
    print("Должник с номером: ", choosed_debtor)
    sum_debt = int(input('Сколько должны? '))
    s += sum_debt

print("Общая сумма долга: ", s)
