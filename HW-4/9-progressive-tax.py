profit = float(input("Введите доход: "))

if profit >= 10000:
    if profit <= 50000:
        tax = 10000 * 0.13 + (profit - 10000) * 0.2
    elif profit > 50000:
        tax = 10000 * 0.13 + (50000 - 10000) * 0.2 + (profit - 50000) * 0.3
else:
    tax = profit * 0.13

print(tax)
    