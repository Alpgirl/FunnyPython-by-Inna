message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

s = ""
alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

alphabet_changed = alphabet[shift:] + alphabet[:shift]
res = [alphabet_changed[alphabet.index(letter)] if letter != " " else " " for letter in message]
for el in res:
    s += str(el)

print("Зашифрованное сообщение:", s)