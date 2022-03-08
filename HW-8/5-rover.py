pos_x, pos_y = 8, 10
print("Условие остановки навигации - команда 'Стоп'")
while (True):
    print("Марсоход находится на позиции ", pos_x, ',', pos_y,
          ", введите команду (W - север, S - юг, A - запад, D - восток): ", sep='')
    command = input()
    if command == 'stop':
        break
    dict_big = {'A': "-1,0", "W": "0,1", "S": "0,-1", "D": "1,0"}
    dict_small = {'a': "-1,0", "w": "0,1", "s": "0,-1", "d": "1,0"}
    try:
        move = dict_big[command].split(',')
    except:
        move = dict_small[command].split(',')
    if 0 <= pos_x + int(move[0]) <= 15 and 0 <= pos_y + int(move[1]) <= 20:
        pos_x += int(move[0])
        pos_y += int(move[1])
