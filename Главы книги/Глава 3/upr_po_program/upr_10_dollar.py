number_1 = int(input('Введите количество монет достоиноством 1 цент '))
number_5 = int(input('Введите количество монет достоиноством 5 центов '))
number_10 = int(input('Введите количество монет достоиноством 10 центов '))
number_25 = int(input('Введите количество монет достоиноством 25 центов '))
number_50 = int(input('Введите количество монет достоиноством 50 центов '))

dollar = 100
cent_1 = 1
cent_5 = 5
cent_10 = 10
cent_25 = 25
cent_50 = 50
sum = (cent_1 * number_1) + (cent_5 * number_5) + (cent_10 * number_10) + (cent_25 * number_25) + (cent_50 * number_50)
if sum == dollar:
    print(f'{sum} центов')
    print('Поздравляем, вы выйграли 1$')
else:
    print(f'{sum} центов')
    print('Увы, вы ничего не выйграли, попробуйте еще раз')