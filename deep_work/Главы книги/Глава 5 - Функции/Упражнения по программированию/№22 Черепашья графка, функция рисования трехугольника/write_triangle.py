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
    triangle(X1, Y1, X2, Y2, 'red')
    triangle(X2, Y2, X3, Y3, 'blue')
    triangle(X1, Y1, X3, Y3, 'purple')
    
def triangle(startX, startY, endX, endY, color):
    turtle.pendown()
    turtle.goto(startX, startY)
    turtle.pencolor(color)
    turtle.goto(endX, endY)
    turtle.pendown()
    
main()

turtle.done()