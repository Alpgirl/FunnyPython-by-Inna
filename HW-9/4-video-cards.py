v_cards = int(input("Количество видеокарт: "))
num = []

for v_card in range(1, v_cards + 1):
    print(v_card, "Видеокарта: ", end="")
    num.append(int(input()))

print("Старый список видеокарт:", num)
new_v_cards = [value for value in num if value != max(num)]
print("Новый список видеокарт:", new_v_cards)

# Убрать запятые из списка: https://pythobyte.com/remove-punctuation-python-98390/
