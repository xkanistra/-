# Эта программа преобразует скорости от 60
# до 130 км/ч (с шагом в 10 км).

START_SPEED = 60 # Начальная сокрость
END_SPEED = 131 # Конечная скорость
INCREMENT = 10 # Шаг скорости
CONVERSION_FACTOR = 0.6214 # Коэф. пересчета

# Напечатать заголовок таблицы
print('KPH\tMPH')
print('-------------')

# Напечатать скорости
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph:.1f}')