text = input("Введите текст: ")
words = text.split(' ')
max_len = len(words[0])
for word in words:
    if len(word) >= max_len:
        max_len = len(word)
print("Самое длинное слово, букв:", max_len)

