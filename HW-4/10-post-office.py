time = int(input("Введите час: "))

if 10 <= time < 12 or 14 <= time < 15 or 18 <= time < 20 or time < 8 or time > 22:
    print("Посылку получить нельзя")
else:
    print("Можно получить посылку")