# Программа рисует фигуры из предложенного меню

import turtle

turtle.speed(5)
turtle.showturtle()

# x и y для положения квадрата
X_QUADRATE = -50
Y_QUADRATE = -50

# x и y для положения квадрата
X_TRIANGLE = -50
Y_TRIANGLE = -29

# Размер восьмигранника
HEXAGONE_STEPS = 80
# Размер стороны квадрата и трехугольника
SIDE = 100
# Угол квадрата
QUADRATE_ANGLE = 90
# Угол трехугольника
TRIANGLE_ANGLE = 120

quadrate = 1
triangle = 2
hexagone = 3

while True:
      print("=== Выбери объект чтобы его ===")
      print("     ~~ Выбор объекта ~~       ")
      print(f"1. Квадрат\n" f"2. Треугольник\n" f"3. Шестиугольник\n" f"4. Выход")

      selection = int(input("Введите номер для операции: "))

      while selection < 1 or selection > 4:
            print("Ошибка, выберите 1 - 4")
            selection = int(input("Введите верный номер операции: "))

      if selection == 1:
            turtle.penup()
            turtle.goto(X_QUADRATE, Y_QUADRATE)
            turtle.pendown()
            for i in range(4):
                  turtle.forward(SIDE)
                  turtle.left(QUADRATE_ANGLE)
            turtle.penup()
            turtle.home()
            turtle.pendown()
            turtle.clearscreen()

      elif selection == 2:
            turtle.penup()
            turtle.goto(X_TRIANGLE, Y_TRIANGLE)
            turtle.pendown()
            for i in range(3):
                  turtle.forward(SIDE)
                  turtle.left(TRIANGLE_ANGLE)
            turtle.penup()
            turtle.home()
            turtle.pendown()
            turtle.clearscreen()

      elif selection == 3:
            turtle.circle(80, steps=8)
            turtle.clearscreen()

      else:
            print("Спасибо за визит <3")
            turtle.done()
