v = float(input("Введите скорость Васи: "))
t = float(input("Введите кол-во часов: "))
len = 115

circles = int(v * t /len)
num_km = int(v*t - len*circles)
print(num_km)