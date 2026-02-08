# Программа рисует выбранный объект из списка

import turtle
turtle.speed(6)
turtle.showturtle()
quadrate = 1
triangle = 2
circle = 3

print('=== Выбери объект чтобы его ===')
print('     ~~ Выбор объекта ~~       ')
print('1.Квадрат\n' \
'2.Трехугольник\n' \
'3.Круг')

selection = int(input('Введите номер объекта: '))

while selection < 1 or selection > 3:
    print('ОШИБКА: неверный диапазон')
    selection = int(input('Введите верный номер объекта: '))
    
    while selection == 1 or selection == 2 or selection == 3:   

        if selection == 1:
            turtle.goto(100, 0)
            turtle.goto(100, 100)
            turtle.goto(0, 100)
            turtle.goto(0, 0)

        elif selection == 2:
            turtle.goto(100, 0)
            turtle.goto(100, 100)
            turtle.goto(0, 0)

        elif selection == 3:
            d = int(input('Введите диаметр круга: '))
            turtle.circle(d)
        
        selection = int(input('Введите номер объекта: '))
        
turtle.done()