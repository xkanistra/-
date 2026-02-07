# Анализ бюджета. Программа считает бюджет пользователя за месяц.

selection = 'Д'

price = float(input('Введите ваш месячный бюджет: '))

total = 0.0

while selection == 'Д' or selection == 'д':
    expenses = float(input('Введите ваш расход: '))
    total += expenses
    selection = input('Есть еще категории расходов? (Д/д - если да) ')

money = price - total
print(f'Ваши расходы сооставляют: {total:.2f}р')
print(f'Остаток остовляет: {money:.2f}р')

if money > 0:
    print(f'Вы сэкономили {money:.2f}р')
elif money < 0:
    print(f'Вы перерасходовали: {money:.2f}р')
    