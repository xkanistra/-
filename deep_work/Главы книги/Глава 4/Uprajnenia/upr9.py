# Уровень океана

MM = 1.6

# year = int(input('Введите количество лет для расчета: '))
total = 0.0
print('Лет \t Подъем')
print('-' * 20)
for y in range(1, 25 + 1):
    mm = y * MM

    print(f"{y} \t {mm:.2f} мм")
