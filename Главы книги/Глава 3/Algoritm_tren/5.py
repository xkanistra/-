amount1 = int(input('Введите значение 1 '))
amount2 = int(input('Введите значение 2 '))
if amount1 > 10 and amount2 < 100 and amount1 < amount2:
    print(amount2)
elif amount1 > 10 and amount2 < 100 and amount1 > amount2:
    print(amount1)
else:
    print('Неверное значение')