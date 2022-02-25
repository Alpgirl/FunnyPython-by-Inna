price = float(input("Введите стоимость квартиры: "))
square = float(input("Введите площадь квартиры: "))

if (price <= 7 and 80 <= square < 100) or (price <= 10 and square >= 100):
    print("Вариант подходит")
else:
    print("Вариант не подходит")
