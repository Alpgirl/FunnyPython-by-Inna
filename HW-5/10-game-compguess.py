import random
from random import randint

num_toguess = int(input("Какое число Вы загадали (от 1 до 100)? "))
cnt = 0
first, last = 1, 100

while(True):
    cnt += 1
    num_guessed = (first + last)//2
    print("Твоё число равно, меньше или больше, чем число (1 — равно, 2 — больше, 3 — меньше)", num_guessed, "?", end = ' ')
    check = int(input())
    if check == 2: first = num_guessed
    elif check == 3: last = num_guessed
    else:
        print("Число угадано! Кол-во попыток: ", cnt)
        exit()
