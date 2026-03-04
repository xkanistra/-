# Программа рисует шахматную доску

import turtle
import square

turtle.speed(10)
turtle.hideturtle()


def main():
    x = 0
    y = 0
    width = 30
    for j in range(1, 6):
        y -= width

        if j % 2 != 0:
            for i in range(1, 6):
                x += width
                if i % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                square.square(x, y, width, color)
            x *= 0
        else:
            for i in range(1, 6):
                x += width
                if i % 2 == 0:
                    color = "black"
                else:
                    color = "white"
                square.square(x, y, width, color)
            x *= 0


main()
