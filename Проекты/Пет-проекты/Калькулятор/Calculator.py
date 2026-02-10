print('=== КАЛЬКУЛЯТОР ===')
print('Список операций')

print(f'1.Сложение')
print(f'2.Вычитание')
print(f'3.Умножение')
print(f'4.Деление')

summation = 1
subtraction = 2
multiplication = 3
division = 4

option = int(input('Выберите номер операции: '))

number_1 = float(input('Выберите первое число '))
number_2 = float(input('Выберите второе число '))

if option == 1:
    sum = number_1 + number_2
    print(f'{sum:.2f}')

elif option == 2:
    sub = number_1 - number_2
    print(f'{sub:.2f}')

elif option == 3:
    mult = number_1 * number_2
    print(f'{mult:.2f}')

elif option == 4 and number_2 != 0:
    div = number_1 / number_2
    print(f'{div:.5f}')

elif option == 4 and number_2 == 0:
    print('Ошибка, на ноль делить нельзя!')

else:
    print('Ошибка, неверный номер операции')
