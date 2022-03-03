marks = input("Введите оценки за сегодняшний день(разделитель - пробел): ")
cnt_3, cnt_4, cnt_5 = 0, 0, 0
for fig in marks:
    if fig == '3':
        cnt_3 += 1
    elif fig == '4':
        cnt_4 += 1
    elif fig == '5':
        cnt_5 += 1
if max(cnt_3, cnt_4, cnt_5) == 5:
    print("Сегодня больше отличников")
elif max(cnt_3, cnt_4, cnt_5) == 4:
    print("Сегодня больше хорошистов")
else:
    print("Сегодня больше троечников")
