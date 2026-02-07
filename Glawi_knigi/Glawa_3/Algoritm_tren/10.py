import turtle

turtle.showturtle()
turtle.goto(0, 100)
turtle.goto(100, 100)
turtle.goto(100, 0)
turtle.goto(0, 0)
turtle.goto(100, 200)
turtle.xcor()
turtle.ycor()
if turtle.xcor() >= 100 and turtle.ycor() >= 100 or turtle.xcor() >= 200 and turtle.ycor() >= 200:
    turtle.hideturtle()
    print('Черепаха в прямоугольнике')
else:
    print('Черепаха вне прямоугольника')
print(turtle.xcor(), turtle.ycor())
turtle.done()