cards_all = int(input("Введите число карточек: "))
numbers_cards = input("Введите номера оставшихся карточек: ")

cards_numbers = numbers_cards.split(" ")
for num in range(1, cards_all + 1):
    if str(num) not in cards_numbers:
        print(num)