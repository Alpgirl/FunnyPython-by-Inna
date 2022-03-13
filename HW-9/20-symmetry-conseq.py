N = int(input("Кол-во чисел: "))
num, res = [], []
i, j, cnt = 0, 0, 0

num = [int(input("Число: ")) for i in range(N)]
num_compare = num.copy()
num_compare.reverse()

print("\nПоследовательность:", *num)

while i < len(num_compare) - cnt:
    if num[j] != num_compare[i]:
        res.insert(0, num[cnt])
        cnt += 1
        j, i = cnt, 0
    i += 1
    j += 1

print("Нужно приписать чисел:", len(res))
if len(res) > 0:
    print("Сами числа:", *res)
