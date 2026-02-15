# Знак STOP.

import turtle

turtle.hideturtle()
turtle.speed(0)

for x in range(8):
    turtle.forward(100)
    turtle.left(45)
turtle.penup()
turtle.goto(50, 120)
turtle.pendown()
turtle.write("STOP", align="center")

turtle.done()
