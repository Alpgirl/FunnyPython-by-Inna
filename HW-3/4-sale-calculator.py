cost1 = int(input("Введите 1-ю стоимость: "))
cost2 = int(input("Введите 2-ю стоимость: "))
cost3 = int(input("Введите 3-ю стоимость: "))

sum = int(cost1+cost2+cost3)
if sum > 10000: print(int(sum * 0.9))
else: print(sum)