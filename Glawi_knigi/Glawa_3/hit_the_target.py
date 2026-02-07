import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LEFT_X = 100
TARGET_LEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

angle = float(input('Введите угол выстрела снаряда: '))
force = float(input('Введите пусковую силу снаряда (1-10): '))

disctance = force * FORCE_FACTOR

turtle.setheading(angle)

turtle.pendown()
turtle.forward(disctance)

if (turtle.xcor() >= TARGET_LEFT_X and turtle.xcor() <= (TARGET_LEFT_X + TARGET_WIDTH) and turtle.ycor() >= TARGET_LEFT_Y and turtle.ycor() <= (TARGET_LEFT_Y + TARGET_WIDTH)):
    print('Цель поражена!')
else:
    print('Вы промахнулись!')

turtle.done()