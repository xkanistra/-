# Программа рисует треугольник
import turtle

turtle.hideturtle()
turtle.speed(10)

X1 = 0
Y1 = 0
X2 = 100
Y2 = 0
X3 = 50
Y3 = 100

def main():
    triangle(X1, Y1, X2, Y2, 'red', 'black')
    triangle(X2, Y2, X3, Y3, 'blue', 'black')
    triangle(X1, Y1, X3, Y3, 'purple', 'black')
    
def triangle(startX, startY, endX, endY, color, color1):
    turtle.fillcolor(color1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(startX, startY)
    turtle.pencolor(color)
    turtle.goto(endX, endY)
    turtle.pendown()
    turtle.end_fill()

main()

turtle.done()