# Средняя толщина дождевых осадков.

year = int(input('Введите кол-во лет: '))
mounth = 12
total = 0.0
for y in range(year):
    for m in range(1, mounth + 1):
        mm = float(input(f'Введите кол-во осадков втечении {m} месяца: '))
        total += mm
average = total / m
all_mounth = year * mounth
print(f'{all_mounth:.0f} \t месяцев')
print('-----------------------')
print(f'{total:.2f} мм в год')
print(f'{average:.2f} мм в месяц')