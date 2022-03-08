text = input("Введите строку для подсчета получаемого молока: ")
if len(text) > 10:
    print("Всего 10 стойл, Вы ввели больше символов. Попробуйте еще раз.")
    exit()
busy_stalls = [i for i, x in enumerate(text) if x == "a"]
litres = 0
for stall in busy_stalls:
    litres += (stall + 1)*2
print(litres)
