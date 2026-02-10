number_5 = int(input('Введите количество монет достоиноством 5 копеек '))
number_10 = int(input('Введите количество монет достоиноством 10 копеек '))
number_50 = int(input('Введите количество монет достоиноством 50 копеек '))

rub = 100
copeika_5 = 5
copeika_10 = 10
copeika_50 = 50
sum = (copeika_5 * number_5) + (copeika_10 * number_10) + (copeika_50 * number_50)
if sum == rub:
    print(sum)
    print('Поздравляем, вы выйграли рубль')
else:
    print(sum)
    print('Увы, вы ничего не выйграли, попробуйте еще раз')