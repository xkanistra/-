# Концентрические круги
import turtle

# Именованный константы
NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10 # Расстояние между кругами
ANIMATION_SPEED = 0

# Настроить черепаху
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Задать радиус первого круга
radius = STARTING_RADIUS

# Нарисовать круги
for count in range(NUM_CIRCLES):
    # Нарисовать круг
    turtle.circle(radius)

    # Получить координты след.круга
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    # Вычислить радиус круга
    radius = radius + OFFSET

    # Позиция черепахи для след круга
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()