N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", K, "человек")

people = [i for i in range(1, N + 1)]
people_copy = people.copy()
ind = 0

while (len(people) > 1):
    print("\nТекущий круг людей:", people)
    print("Начало счёта с номера", people_copy.index(people[ind]) + 1)

    ind += K - len(people) * (K//len(people)) - 1
    if ind >= len(people): ind -= len(people)
    elif ind == -1: ind = len(people) - 1
    print("Выбывает человек под номером", people_copy.index(people[ind]) + 1)
    people.remove(people[ind])
    if ind >= len(people): ind -= len(people)

print("\nОстался человек под номером", people_copy.index(people[0]) + 1)

# Доделать вывод правильных индексов!