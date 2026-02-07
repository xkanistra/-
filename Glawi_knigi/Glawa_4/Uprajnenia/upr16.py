# Повторение квадратов.
import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.setup(1000, 1000)
start_long = 300
angle = 90
turtle.left(90)

# цикл задает размер повторяясь 100 раз после рисования квадрата
for long in range(100):  
    start_long -= 3
    # цикл рисует квадрат на каждый цикл увеличения
    for quadrate in range(4):  
        turtle.forward(start_long)
        turtle.left(angle)

turtle.done()
