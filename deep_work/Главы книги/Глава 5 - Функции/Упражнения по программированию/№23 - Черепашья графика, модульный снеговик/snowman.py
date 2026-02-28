# Программа рисует снеговика

import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.setup(1920, 1080)
X1 = 0
Y1 = 0
X2 = 0
Y2 = 200
X3 = 0
Y3 = 350
RADIUS_1 = 100
RADIUS_2 = 75
RADIUS_3 = 50
LEFT_ARM_X = -75
LEFT_ARM_Y = 275
END_X = -175
END_Y = 325
RIGHT_ARM_X = 75
RIGHT_ARM_Y = 275
RIGHT_X = 175
RIGHT_Y = 325

X1_EYE = -15
Y1_EYE = 400
EYE1_RADIUS = 5
X2_EYE = 15
Y2_EYE = 400
EYE2_RADIUS = 5

X1_FACE = -15
Y1_FACE = 380
X2_FACE = 15
Y2_FACE = 380

X_HAT = -75
Y_HAT = 425
ANGLE = 90


def main():
    drawBaze(X1, Y1, RADIUS_1)
    drawMidSection(X2, Y2, RADIUS_2)
    drawHead(
        X3,
        Y3,
        RADIUS_3,
        X1_EYE,
        Y1_EYE,
        EYE1_RADIUS,
        X2_EYE,
        Y2_EYE,
        EYE2_RADIUS,
        X1_FACE,
        Y1_FACE,
        X2_FACE,
        Y2_FACE,
    )
    drawArms(LEFT_ARM_X, LEFT_ARM_Y, END_X, END_Y)
    drawArms(RIGHT_ARM_X, RIGHT_ARM_Y, RIGHT_X, RIGHT_Y)
    drawHat(X_HAT, Y_HAT, ANGLE, 'black')


def drawBaze(x, y, radius):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()


def drawMidSection(x, y, radius):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()


def drawHead(x, y, radius, x1, y1, eye1, x2, y2, eye2, xface1, yface1, xface2, yface2):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.circle(eye1)
    turtle.penup()
    turtle.goto(x2, y2)
    turtle.pendown()
    turtle.circle(eye2)
    turtle.penup()
    turtle.goto(xface1, yface1)
    turtle.pendown()
    turtle.goto(xface2, yface2)
    turtle.penup()


def drawArms(x, y, endX, endY):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(endX, endY)
    turtle.penup()


def drawHat(x, y, angle, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(150)
    turtle.left(angle)
    turtle.forward(30)
    turtle.left(angle)
    turtle.forward(30)
    turtle.right(angle)
    turtle.forward(30)
    turtle.left(angle)
    turtle.forward(90)
    turtle.left(angle)
    turtle.forward(30)
    turtle.right(angle)
    turtle.forward(30)
    turtle.left(angle)
    turtle.forward(30)
    turtle.left(angle)
    turtle.end_fill()
main()
turtle.done()
