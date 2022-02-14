income_quarter_1 = float(input("Введите сумму дохода за 1-й квартал: "))
income_quarter_2 = float(input("Введите сумму дохода за 2-й квартал: "))
income_quarter_3 = float(input("Введите сумму дохода за 3-й квартал: "))
income_quarter_4 = float(input("Введите сумму дохода за 4-й квартал: "))

sum1 = income_quarter_1 + income_quarter_2
sum2 = income_quarter_3 + income_quarter_4

res = sum1/sum2

print("Динамика: ", res)