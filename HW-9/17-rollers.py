num_skates = int(input("Кол-во коньков: "))
size_pair, size_human = [], []

for i in range(1, num_skates + 1):
    print("Размер", i, "пары: ", end="")
    size_pair.append(int(input()))

num_people = int(input("\nКол-во людей: "))

for i in range(1, num_people + 1):
    print("Размер ноги", i, "человека: ", end="")
    size_human.append(int(input()))

lst = [min(size_human.count(size), size_pair.count(size)) for size in list(set(size_human))]
print("\nНаибольшее кол-во людей, которые могут взять ролики: ", sum(lst))
