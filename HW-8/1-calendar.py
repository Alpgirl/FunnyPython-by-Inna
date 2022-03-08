week_day = input("Введите день недели: ")
week_days_big = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
week_days_small = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
try:
    res = week_days_big.index(week_day) + 1
except:
    res = week_days_small.index(week_day) + 1
print("Номер дня недели:", res)
