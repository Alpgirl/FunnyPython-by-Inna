import random
from random import randint

cnt = 0
num_toguess = random.randint(0, 20)
while (True):
    cnt += 1
    num_try = int(input("Введите число: "))
    if num_try < num_toguess: print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif num_try > num_toguess: print("Число больше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали! Число попыток: ", cnt)
        exit()
