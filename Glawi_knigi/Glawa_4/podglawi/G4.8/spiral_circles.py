# Программа рисует узор, используя повторяющиеся круги.
import turtle

# Именованный константы
NUM_CIRCLES = 36        # Кол-во кругов
RADIUS = 100            # Радиус кругов
ANGLE = 10            # Угол поворота
ANIMATION_SPEED = 0     # Скорость анимации

# Задать скорость анимации
turtle.speed(ANIMATION_SPEED)

# Нарисовать 36 кругов, наклоняя черепаху на
# 10 градусов после того, как каждый круг был нарисован
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)