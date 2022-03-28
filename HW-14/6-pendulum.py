try:
    ampl_start = float(input('Введите начальную амплитуду: '))
    ampl_stop = float(input('Введите амплитуду остановки: '))
except:
    exit('Неверный ввод данных')

if ampl_start < ampl_stop or ampl_start < 0 or ampl_stop < 0: exit('Неверный ввод данных')
cnt = 0

while ampl_start >= ampl_stop:
    cnt += 1
    ampl_start -= 0.084 * ampl_start

print('Маятник считается остановившимся через', cnt, 'колебаний')
