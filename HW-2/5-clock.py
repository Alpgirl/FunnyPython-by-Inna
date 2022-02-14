minutes = int(input("Введите кол-во минут: "))

hours = int(minutes/60)
minutes -= hours*60
print("Время: ", hours, ":", minutes, ":", "0")