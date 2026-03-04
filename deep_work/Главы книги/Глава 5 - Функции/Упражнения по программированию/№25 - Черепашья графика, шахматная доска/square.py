import turtle

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