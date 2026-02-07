# Потеря массы

mass = float(input('Введите ваш текущий вес в кг: '))

print('-' * 3, 'Прогнозируемое снижение веса', '-' * 3)
print('Месяц\t\tВес')
for m in range(1, 6 + 1):
    mass -= 1.5

    print(f'{m}\t\t{mass:.2f} кг')
