# Программа рисует фигуру по паттерну

import turtle

ANGLE = 90
ANGLE_LINE = 45
turtle.hideturtle()
turtle.speed(10)


def main():
    lendth = float(input("Длина: "))
    width = float(input("Ширина: "))
    drawPattern(lendth, width, "black")


def drawPattern(lendth, width, color):

    for c in range(2):
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.forward(lendth)
        turtle.left(ANGLE)
        turtle.forward(width)
        turtle.left(ANGLE)
        turtle.end_fill()

    turtle.penup()
    turtle.goto(-10, -10)
    turtle.pendown()

    lendth += 20
    width += 20

    for i in range(2, 4):
        turtle.forward(lendth)
        turtle.left(ANGLE)
        turtle.forward(width)
        turtle.left(ANGLE)

    turtle.penup()
    turtle.goto(-20, -20)
    turtle.pendown()

    lendth += 20
    width += 20

    for i in range(2, 4):
        turtle.forward(lendth)
        turtle.left(ANGLE)
        turtle.forward(width)
        turtle.left(ANGLE)

    #turtle.goto(120, 120)
    #turtle.goto(-20, 120)
    #turtle.goto(120, -20)
    #turtle.goto(120, 50)
    #turtle.goto(-20, 50)


#print(turtle.xcor(), turtle.ycor())
main()
turtle.done()
