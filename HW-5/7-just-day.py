print("Начался 8-часовой рабочий день")
hour, tasks = 1, 0
flag = False
while(hour < 9):
    print(hour, "-й час", sep = '')
    tasks += int(input("Сколько задач решит Максим? "))
    call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if call == 1: flag = True
    hour += 1

print("Рабочий день закончился. Всего выполнено задач: ", tasks)
if flag == True: print("Нужно зайти в магазин.")
