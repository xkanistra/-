# Программа рисует узор, используя повторяющиеся линии.
import turtle

# Именованный константы
START_X = -200          # Стартовая координата х
START_Y = 0             # Стартовая координата y
NUM_LINES = 36          # Кол-во линий
LINE_LENGHT = 400       # Длинна линии
ANGLE = 170             # Угол поворота
ANIMATION_SPEED = 0     # Скорость анимации

# Переместить черепаху в начальную позицию
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

# Задать скорость
turtle.speed(ANIMATION_SPEED)

# Нарисовать 36 линий наклоняя черепаху
# на 170 градусов после того, как каждая линия была нарисована.
for x in range(NUM_LINES):
    turtle.forward(LINE_LENGHT)
    turtle.left(ANGLE)