check = False
cnt = 0

while (check == False):
    attempt = input("Придумайте пароль: ")
    if len(attempt) > 8:
        for sym in attempt:
            if sym.isupper() == True or sym.isdigit():
                cnt += 1
    if cnt > 3:
        check = True
        print("Это надёжный пароль!")
    else: print("Пароль ненадёжный. Попробуйте ещё раз.")
