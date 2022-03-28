def print_in_lines(dict):
    return [print(key,':',value) for key, value in dict.items()]

text = input('Введите текст: ')
orig_dict, inv_dict = {}, {}

for i in list(set(text)):
    ind = [k for k,v in enumerate(text) if v == i]
    orig_dict[i] = len(ind)
print("Оригинальный словарь частот:")
print_in_lines(orig_dict)

for i in list(set(orig_dict.values())):
    inv_dict[i] = [key for key,value in orig_dict.items() if value == i]
print("\nИнвертированный словарь частот:")
print_in_lines(inv_dict)