string = list(input('Введите строку: '))
dict_sym, cnt = {}, 0

for val in set(string):
    amounts = [v for v in string if v == val]
    dict_sym[val] = len(amounts)
for val in dict_sym.values():
    if val%2 != 0:
        cnt += 1
if cnt > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')