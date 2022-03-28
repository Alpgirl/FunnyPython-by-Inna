#N = int(input('Введите кол-во заказов: '))
dict_orders = {'1 заказ': 'Иванов Пепперони 1',
                '2 заказ': 'Петров Де-Люкс 2',
                '3 заказ': 'Иванов Мясная 3',
                '4 заказ': 'Иванов Мексиканская 2',
                '5 заказ': 'Иванов Пепперони 2',
                '6 заказ': 'Петров Интересная 5',
                '7 заказ': 'Соловьев Интересная 8',
                '8 заказ': 'Артемьев Мясная 3'}
def parse(dict):
    values = [val.split() for val in dict.values()]
    return values
def print_in_lines(dict):
    return [print(" "*2, key,': ',value, sep ="") for key, value in sorted(dict.items()) if value != 0]

dict_report = {}
surname = list(set([lst[0] for lst in parse(dict_orders)]))
pizza_name = list(set([lst[1] for lst in parse(dict_orders)]))

for buyer in sorted(surname):
    for pizz in pizza_name:
        dict_report[pizz] = 0
    for el in parse(dict_orders):
        if buyer == el[0]:
            dict_report[el[1]] = dict_report[el[1]] + int(el[2])
    print(buyer, ":", sep="")
    print_in_lines(dict_report)