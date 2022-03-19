N = int(input("Кол-во палок: "))
K = int(input("Кол-во бросков: "))

res = ['|'] * N
s = ""

for i in range(1, K+1):
    print("Бросок ", i, ". Сбиты палки с номера ", end="", sep="")
    L = int(input())
    print("по номер ", end="")
    R = int(input())
    for i in range(L-1, R):
        if res[i] == '|':
            res[i] = '.'

for el in res:
    s += str(el)

print("Результат:", s)




