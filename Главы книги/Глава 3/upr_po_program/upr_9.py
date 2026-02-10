carman_number = int(input('Введите номер кармана от 0 до 36 '))

if carman_number == 0:
    print('Зеленый')

elif carman_number >= 1 and carman_number <= 10 and carman_number % 2 == 0:
    print('Черный')
elif carman_number >= 1 and carman_number <= 10 and carman_number % 2 != 0:
    print('Красный')

elif carman_number >= 11 and carman_number <= 18 and carman_number % 2 == 0:
    print('Красный')
elif carman_number >= 11 and carman_number <= 18 and carman_number % 2 != 0:
    print('Черный')

elif carman_number >= 19 and carman_number <= 28 and carman_number % 2 == 0:
    print('Черный')
elif carman_number >= 19 and carman_number <= 28 and carman_number % 2 != 0:
    print('Красный')

elif carman_number >= 29 and carman_number <= 36 and carman_number % 2 == 0:
    print('Красный')
elif carman_number >= 29 and carman_number <= 36 and carman_number % 2 != 0:
    print('Черный')

else:
    print('Ошибка, вышли за диапазон от 0 до 36')
