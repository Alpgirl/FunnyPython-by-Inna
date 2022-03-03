input = input("Введите 10 чисел (разделитель - пробел): ")
numbers = input.split(" ")
pos = 0
for num in numbers:
    num = int(num)
    if num % 2 == 0 and num > 0:
        pos += 1
print("Количество должников: ", pos)