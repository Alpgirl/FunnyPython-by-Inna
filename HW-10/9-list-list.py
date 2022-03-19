nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
res = [el for lst1 in nice_list for lst2 in lst1 for el in lst2]

print("Ответ:", res)