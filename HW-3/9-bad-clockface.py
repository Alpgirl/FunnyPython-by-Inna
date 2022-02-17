mileage = input("Введите пробег: ")
day = int(input("Введите сегодняшнее число: "))
cnt = 0
sum = 0

if day > 31:
    print("Неверная дата")
    exit()

cnt = len(mileage)
mileage = int(mileage)
forsave = mileage
for i in range(0, cnt):
    sum += mileage % 10
    mileage //= 10

if sum > day: print(" Сброс\n", "Пробег: 0")
else: print(" Сегодня не сломался\n", "Пробег:", forsave)