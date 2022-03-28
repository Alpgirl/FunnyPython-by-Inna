#N = int(input("Введите количество пар слов: "))
dict_syn = {'1 пара': 'Привет - Здравствуйте',
            '2 пара': 'Печально - Грустно',
            '3 пара': 'Весело - Радостно',
            '4 пара': 'Дом - Здание',
            '5 пара': 'Телефон - Мобильник',
            '6 пара': 'Папка - Каталог'}

def parse(dict):
    values = [val.split(' - ') for val in dict.values()]
    return values

while (True):
    lst, torememb = [], []
    word = input('Введите слово: ')
    for el in parse(dict_syn):
        lst = [el[len(el) - el.index(word) - 1] for el2 in el if word in el2]
        if lst:
            torememb = lst
    print('Синоним:', *torememb) if torememb else print('Такого слова в словаре нет.')