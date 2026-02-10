# Гипнотический узор.

import turtle

turtle.showturtle()
turtle.speed(0)
turtle.setup(1000, 1000)
start_long = 1
angle = 90

for q in range(100):
    turtle.forward(start_long)
    turtle.left(angle)
    for l in range(10):
        start_long += 0.5
        
turtle.done()
