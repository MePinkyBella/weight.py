weight = float(input("Введите массу тела (в килограммах): "))
distance = float(input("Введите расстояние (в метрах): "))
time = float(input("Введите время (в секундах): "))
velocity = ((2 * weight * distance) / time) ** 0.5
print("Скорость равна", velocity, "м/с")
