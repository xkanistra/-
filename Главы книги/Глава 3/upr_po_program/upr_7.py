color_1 = input('Введите один из основнызх цветов ')
color_2 = input('Введите один из основнызх цветов ')

red = 'Красный'
blue = 'Синий'
yellow = 'Желтый'

purple = 'Фиолетовый'
orange = 'Оранжевый'
green = 'Зеленый'

if color_1 == red and color_2 == blue or color_1 == blue and color_2 == red:
    print(purple)
elif color_1 == red and color_2 == yellow or color_1 == yellow and color_2 == red:
    print(orange)
elif color_1 == blue and color_2 == yellow or color_1 == yellow and color_2 == blue:
    print(green)
else:
    print('Ошибка')