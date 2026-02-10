day = int(input('Введите день '))
mounth = int(input('Введите месяц '))
year = int(input('Введите двухзначный год(последние два числа года) '))

if day * mounth == year:
    print('Дата является магической')
else:
    print('Дата не является магической')