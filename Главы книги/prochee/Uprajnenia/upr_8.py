eat = float(input('Введите стоимость всех блюд '))
TIPS = 0.18
TAX = 0.08
eat_tips = eat * TIPS
eat_tax = TAX * eat
print(f'Стоимость блюд составляет: {eat:.2f} р\n'
      f'Кол-во чаевых составляет: {eat_tips:.2f} р\n'
      f'Размер нлога составляет: {eat_tax:.2f} р\n'
      f'Общая стоимость состовляет: {eat + eat_tax + eat_tips:.2f} р')