message = input("Введите строку: ") + ' '
cnt, max_cnt = 0, 0
for sym in message:
    if sym == 's':
        cnt += 1
    else:
        max_cnt = cnt if cnt >= max_cnt else max_cnt
        cnt = 0
print(max_cnt)
