max_num = int(input('Введите максимальное число: '))
lst_remain = [j for j in range(1, max_num+1)]
num_guessed = 7
while(True):
    nums = input('\nНужное число есть среди вот этих чисел: ')
    if nums == 'Помогите!':
        print('Артём мог загадать следующие числа:', *lst_remain)
        break
    if max(int(i) for i in nums.split()) > max_num:
        exit('Введено число больше максимального')

    print('Ответ Артема: ', end="")
    if num_guessed in [int(i) for i in nums.split()]: print('Да')
    else:
        print('Нет')
        [lst_remain.pop(lst_remain.index(el)) for el in [int(i) for i in nums.split()] if el in lst_remain]