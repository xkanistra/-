import turtle
import random

def sky(color_sky, color_star):
    turtle.fillcolor(color_sky)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.end_fill()
    for j in range(10):
        turtle.fillcolor(color_star)
        turtle.begin_fill()
        x = random.randrange(0, 200, 10)
        y= random.randrange(50, 200, 10)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(3)
        turtle.end_fill()
    turtle.home()