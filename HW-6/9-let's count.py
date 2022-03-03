input = input("Введите 10 чисел (разделитель - пробел): ")
numbers = input.split(" ")
size = len(numbers) - 1
order = True

for ind in range(size):
    if int(numbers[ind]) >= int(numbers[ind + 1]):
        order = False

if order == False:
    print("Числа не упорядочены по возрастанию")
else:
    print("Числа упорядочены по возрастанию")