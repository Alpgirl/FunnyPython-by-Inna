for sector in range(30, 36):
    print("Людей в ", sector, "-м секторе: ", end="", sep="")
    people_in_sector = int(input())
    if people_in_sector > 10:
        print("Нарушение! Слишком много людей в секторе!")
    else:
        print("Всё спокойно.")