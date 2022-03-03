for num in range(1, 100):
    mult = 1
    tosave = num
    while(num != 0):
        mult *= (num % 10)
        num = num//10
    if mult * 3 == tosave:
        print(tosave)
