year = int(input('Введите год '))

if year % 100 == 0 and year % 400 ==0:
    print('29 дней')
    print(f'{year} год високосный')

elif year % 100 != 0 and year % 4 == 0:
    print('29 дней')
    print(f'{year} год високосный')

else:
    print('28 дней')
    print(f'{year} год не високосный')
