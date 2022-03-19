text = input("Введите текст: ")

vowels = "аАуУоОыЫиИэЭяЯюЮёЁеЕ"
resLst = [s for s in text if s in vowels]

print("Список гласных букв:", resLst)
print("Длина списка:", len(resLst))
