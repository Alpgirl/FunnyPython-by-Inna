list1 = [1, 2, 3]
list2 = [2, 4, 6, 3, 3, 2, 1]

print("Первый список:", list1)
print("Второй список:", list2)

list1 = list(set(list1)) + list(set(list2) - set(list1))

print("Новый первый список с уникальными элементами:", list1)