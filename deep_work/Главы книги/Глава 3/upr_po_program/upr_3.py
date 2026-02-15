year = float(input('Введите ваш возраст:'))

if year <= 1:
    print('Младенец')
elif 1 < year < 13:
    print('Ребенок')
elif 13 < year < 20:
    print('Подросток')
elif year >= 20:
    print('Взрослый')