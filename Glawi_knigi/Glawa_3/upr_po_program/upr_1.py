day_week = int(input('Введите день недели '))
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7
if day_week == Monday:
    print('Понедельник')
elif day_week == Tuesday:
    print('Вторник')
elif day_week == Wednesday:
    print('Среда')
elif day_week == Thursday:
    print('Четверг')
elif day_week == Friday:
    print('Пятница')
elif day_week == Saturday:
    print('Суббота')
elif day_week == Sunday:
    print('Воскресенье')
else:
    print('Ошибка диапазона')