num_Kostya = int(input("Кубик Кости: "))
num_host = int(input("Кубик владельца: "))

if num_host < 7 and num_Kostya < 7:
    if num_Kostya >= num_host:
        dif = num_host - num_Kostya
        print("Разность:", dif, "тыс.$")
        print("Костя платит")
    else:
        sum = num_host + num_Kostya
        print("Сумма:", sum, "тыс.$")
        print("Владелец платит")
    print("Игра окончена")
else:
    print("Неверный формат данных")