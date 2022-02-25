num = int(input("Введите количество опыта: "))

if num < 1000:
    res = 1
elif 1000 <= num < 2500:
    res = 2
elif 2500 <= num < 5000:
    res = 3
else:
    res = 4

print("Ваш уровень: ", res)

