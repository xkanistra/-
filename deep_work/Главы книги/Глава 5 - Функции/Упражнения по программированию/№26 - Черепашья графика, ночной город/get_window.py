import turtle
import random

def window_print(x, y, len, color, pencolor, angle):
 
    for i in range(4):
        y += 10
       
        for j in range(1):
            turtle.pencolor(pencolor)
            turtle.fillcolor(color)
            turtle.begin_fill()
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            for i in range(4):
                turtle.forward(len)
                turtle.left(angle)
            turtle.end_fill()




