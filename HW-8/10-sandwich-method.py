encrypted_message = input("Введите зашифрованное сообщение: ")
last_indice = len(encrypted_message) - 1
word = [None] * len(encrypted_message)
cnt = 1

for sym in encrypted_message:
    if cnt % 2 == 0 and cnt != 0:
        word[last_indice - (cnt - 2)//2] = sym
    else:
        word[(cnt - 1)//2] = sym
    cnt += 1

print(''.join(str(e) for e in word))