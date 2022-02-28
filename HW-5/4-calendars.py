num, res = 1, 0
while (num != 0):
#i = [int(a) for a in input().split()] на будущее
    num = int(input())
    if (num % 2 == 0) :
        res += 1
print("Количество четных цифр: ", res)
