num_rows = int(input("Введите кол-во рядов: "))
num_seats = int(input("Введите кол-во сидений в ряде: "))
metres = int(input("Введите кол-во метров между рядами: "))

row, distance = '', ''
row = '=' * num_seats
distance = '*' * metres

row = row + ' ' + distance + ' ' + row + '\n'

print(row*num_rows)
    #print('=', end = '')
