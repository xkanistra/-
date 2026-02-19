import turtle

def main():
    turtle.hideturtle()
    circles(0, 0, 100, 'red')
    circles(-150, -75, 50, 'purple')
    circles(-200, 150, 75, 'black')

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

main()