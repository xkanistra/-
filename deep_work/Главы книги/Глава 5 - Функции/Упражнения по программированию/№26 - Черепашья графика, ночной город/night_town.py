# Программа рисует ночной город
import turtle
import get_window
import get_sky
ANGLE = 90
X_WIND = 10
Y_WIND1 = 5
LENDTH = 5

turtle.hideturtle()
turtle.speed(0)

def main():
    color_house = 'gray'
    color_window = 'yellow'
    sky = 'black'
    star = 'yellow'
    pencolor = 'black'
    get_sky.sky(sky, star)
    build(color_house)
    get_window.window_print(X_WIND, Y_WIND1, LENDTH, color_window, pencolor, ANGLE)
    get_window.window_print(X_WIND + 20, Y_WIND1, LENDTH, color_window, pencolor, ANGLE)
    get_window.window_print(X_WIND + 40, Y_WIND1, LENDTH, color_window, pencolor, ANGLE)
    get_window.window_print(X_WIND + 60, Y_WIND1, LENDTH, color_window, pencolor, ANGLE)
    get_window.window_print(X_WIND + 80, Y_WIND1, LENDTH, color_window, pencolor, ANGLE)
    get_window.window_print(X_WIND + 100, Y_WIND1, LENDTH, color_window, pencolor, ANGLE)
    get_window.window_print(X_WIND + 120, Y_WIND1, LENDTH, color_window, pencolor, ANGLE)
    get_window.window_print(X_WIND + 140, Y_WIND1, LENDTH, color_window, pencolor, ANGLE)
    
def build(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(200)
    turtle.left(ANGLE)
    
    turtle.forward(40)
    turtle.left(ANGLE)
    
    turtle.forward(30)
    turtle.right(ANGLE)
    
    turtle.forward(50)
    turtle.left(ANGLE)
    
    turtle.forward(50)
    turtle.left(ANGLE)
    
    turtle.forward(30)
    turtle.right(ANGLE)
    
    turtle.forward(30)
    turtle.right(ANGLE)
    
    turtle.forward(100)
    turtle.left(ANGLE)
    
    turtle.forward(40)
    turtle.left(ANGLE)
   
    turtle.forward(100)
    turtle.right(ANGLE)
    
    turtle.forward(50)
    turtle.left(ANGLE)
    
    turtle.forward(60)
    turtle.left(ANGLE)
    turtle.end_fill()
    
main()
turtle.done()