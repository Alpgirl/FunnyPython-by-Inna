N = int(input("Введите количество секунд до взрыва: "))
for i in range(N, -1, -1):
    #print(i, " секунд до взрыва")
    answer = input("Хотите обезвредить бомбу? ")
    if answer == "да" or answer == "Да":
        print("Бомба обезврежена за ", i, " секунд")
        break
    elif i == 0:
        print("Бомба взорвалась.")
    else:
        print("До взрыва осталось ", i, " секунд")
