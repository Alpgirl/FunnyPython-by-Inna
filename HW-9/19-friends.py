N = int(input("Кол-во друзей: "))
K = int(input("Долговых расписок: "))
res = [0] * N

for i in range(1, K+1):
    print("\n", i, " расписка", sep ="")
    to_per = int(input("Кому: "))
    from_per = int(input("От кого: "))
    cost = int(input("Сколько: "))
    res[to_per - 1] -= cost
    res[from_per - 1] += cost


print("\nБаланс друзей:")
for s in res:
    print(res.index(s) + 1, ":", s)


