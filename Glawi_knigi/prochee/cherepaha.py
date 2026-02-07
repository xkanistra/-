# ТУТ НЕБОЛЬШАЯ ШПОРГАЛКА ДЛЯ ГРАФИКИ!

import turtle

turtle.bgcolor('cyan') #задает размер

turtle.pensize(5)  # размер пера

turtle.pencolor("blue")  # задает цвет пера

turtle.speed(10)  # скорость пера, от 0 - 10, если 0 то анимации нету, самая медленная скорость 1, самая быстрая 10

turtle.setup(1000, 1000)  # устанавливает размер окна с (высота, ширина) размерами

turtle.showturtle()  # показывает черепаху

turtle.forward(200)  # перемещает черепаху на 200 пикселей вперед

turtle.right(90)  # поворачивает вправо на (n) угол
turtle.forward(200)

turtle.left(90)  # поворачивает влево на (n) угол
turtle.forward(200)

turtle.setheading(90)  # устанавливает угол направления черепахи от изначальной точки на (n) градусов
turtle.forward(200)

turtle.heading()  # показывает текущее угловое значение черепахи

turtle.penup()  # поднимает перо(не рисует линию)
turtle.forward(50)
turtle.pencolor("red")

turtle.pendown()  # опускает перо(рисует линию)
turtle.forward(100)
turtle.penup()
turtle.forward(50)

turtle.dot() # создает точку
turtle.pendown()
turtle.forward(100)
turtle.dot()
turtle.left(90)
turtle.penup()
turtle.forward(200)
turtle.dot()
turtle.pendown()

turtle.reset() # стирает что нарисованно в окне, не переустанавливает фон

turtle.circle(50)  # рисует круг с (n) радиусом
turtle.goto(0, 0)  # перемещает перо по осям X и Y
turtle.goto(0, 100)
turtle.goto(-100, 0)
turtle.goto(0, 0)

turtle.pos()  # получение текущей позиции черпахи по X и Y
turtle.xcor()  # получение текущей позиции черпахи по X
turtle.ycor()  # получение текущей позиции черпахи по Y
turtle.hideturtle()  # скрывает черепаху

turtle.write("Соси хуй")  # вывод текста в графическом окне

turtle.left(80)
turtle.forward(100)
turtle.begin_fill()  # используется для заполнения геометрической фигуры(пишется до фигуры)
turtle.circle(50)
turtle.end_fill()  # используется для заполнения геометрической фигуры(пишется после фигуры)

turtle.left(80)
turtle.forward(100)
turtle.fillcolor("cyan")  # используется для задания цвета фигуры
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.clear() # стирает рисунки

turtle.numinput("Заголовок", "Подсказка")  # используется для создания диалогового окна и манипуляция им
turtle.forward(200)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()

turtle.clearscreen() # делает все настройки черепахи дефолтными

# turtle.numinput('заголовок', 'подсказка?', default=x, minval=y, maxval=z). default=x - устанавливает значение которое будет выводится в поле ввода по умолчанию
# default=x - устанавливает значение которое будет выводится в поле ввода по умолчанию которым является 'x'
# minval=y - устанавливает значение которое будет отклолять любое вводимое число которое меньше 'y'
# maxval=z - устанавливает значение которое будет отклонять любое вводимое число которое больше 'z'

turtle.numinput("Число", "введите число от 1 - 10", default=5, minval=1, maxval=10)

name = turtle.textinput("Как вас зовут?", "Введите ФИО")  # textinput() выводит текст в терминале, можно использовать для записи переменных
print(name)

turtle.done()  # оставляет графическое окно

turtle.clearscreen() # делает все настройки черепахи дефолтными

