header_len = int(input("Введите длину колонтитула: "))
sym_len = int(input("Введите кол-во знаков '!': "))
sym, space = '', ''
space = '~' * ((header_len - sym_len)//2)
sym =  '!' * sym_len

res = space + sym + space
if (header_len - sym_len)//2 + sym_len < header_len:
    res += '~'

print(res)

