order = float(input("Введите место в списке поступающих: "))
grade = float(input("Введите количество баллов за экзамены: "))

if order > 10:
    print("К сожалению, вы не поступили.")
else:
    print("Поздравляем, вы поступили!")
    if grade >= 290:
        print("Бонусом вам будет начисляться стипендия.")
    else:
        print("Но вам не хватило баллов для стипендии.")
