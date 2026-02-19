import turtle

# Функция square рисует квадрат.
# Параметры x и y - это координаты левого нижнего угла
# Параметр width - ширина стороны квадрата
# Параметр color - цвет заливки в виде строки 
def square(x, y, width, color):
    turtle.penup()                  # Поднять перо
    turtle.goto(x, y)               # Переместить в указанное место
    turtle.fillcolor(color)         # Задать цвет заливки
    turtle.pendown()                # Опустить перо
    turtle.begin_fill()             # Начать заливку
    for count in range(4):          # Нарисовать квадрат
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()               # Заверишить заливку

# Функция circles рисует круг.
# Параметры x и y - это координаты центра
# Параметр radius - радиус круга
# Параметр color - цвет заливки в виде строки 
def circles(x, y, radius, color):
    turtle.penup()                      # Поднять перо
    turtle.goto(x, y - radius)          # Переместить в указанное место
    turtle.fillcolor(color)             # Задать цвет заливки
    turtle.pendown()                    # Опустить перо
    turtle.begin_fill()                 # Начать заливку
    turtle.circle(radius)               # Нарисовать круг
    turtle.end_fill()                   # Заверишить заливку

# Функция line рисует отрезок от (startX, startY) до (endX, endY)
# color - цвет отрезка
def line(startX, startY, endX, endY, color):
    turtle.penup()                          # Поднять перо
    turtle.goto(startX, startY)             # Переместить в начальную точку
    turtle.pendown()                        # Опустить перо
    turtle.pencolor(color)                  # Задать цвет заливки пера
    turtle.goto(endX, endY)                 # Нарисовать треугольник