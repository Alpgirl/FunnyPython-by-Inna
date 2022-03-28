#N_people = int(input('Введите количество человек: '))
dict_pedigree = {'1 пара': 'Alexei Peter_I',
                 '2 пара': 'Anna Peter_I',
                 '3 пара': 'Elizabeth Peter_I',
                 '4 пара': 'Peter_II Alexei',
                 '5 пара': 'Peter_III Anna',
                 '6 пара': 'Paul_I Peter_III',
                 '7 пара': 'Alexander_I Paul_I',
                 '8 пара': 'Nicholaus_I Paul_I' }

def print_in_lines(dict):
    return [print(key,value) for key, value in sorted(dict.items())]

people = set([val.split()[0] for val in dict_pedigree.values()] + [val.split()[0] for val in dict_pedigree.values()])
dict_height, height = {}, 0
ancestors = [val.split()[1] for val in dict_pedigree.values() if val.split()[1] not in list(set(val.split()[0] for val in dict_pedigree.values()))]
dict_height[ancestors[0]] = height

while(people != set()):
    height += 1
    children = []
    for val in dict_pedigree.values():
        if val.split()[1] in ancestors:
            children.append(val.split()[0])
        for child in children:
            dict_height[child] = height
    people -= set(children)
    ancestors = children

print('"Высота" каждого члена семьи:')
print_in_lines(dict_height)