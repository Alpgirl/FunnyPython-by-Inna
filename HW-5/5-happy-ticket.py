def sumer(str):
    cnt, sum = 0, 0
    while(cnt < len(str)):
        sum += int(str[cnt])
        cnt += 1
    return sum

ticket_num = input("Введите номер билета: ")

f_part = ticket_num[:len(ticket_num)//2]
l_part = ticket_num[len(ticket_num)//2:]

if (sumer(f_part) == sumer(l_part)):
    print("У вас в кармане счастливый билет!")
else:
    print("У вас в кармане НЕсчастливый билет!")
