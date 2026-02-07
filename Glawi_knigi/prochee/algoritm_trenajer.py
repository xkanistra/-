# Алогометрический тренажер стр. 122
 
# 1.
height = input("Введи свой рост:")
print(f'Твой рост {height} см')

# 2.
color = input('Введи свой любимый цвет:')
print(f'Твой любимый цвет {color:>10}')

# 3.
PI = 3.14
a = 0
c = 2
b = a + c
a = b * 4
b = a / PI
a = b - 8
print(f'{a:.2f}')

# 4.
w = 5
x = 4
y = 8
z = 2
result = x + y
result = z * 2
result = y / x
result = y - z
result = w // z
print(f'Значение переменной равняется {result}')

# 5.
total = 10 + 14
print(total)

# 6.
#due = down_payment - total

# 7.
# total = subtotal * 0.15

# 10.
sales = 15.156
print(f'{sales:.2f}')

# 11.
number = 1234567.456
print(f'{number:,.1f}')

import turtle

# 13.
#turtle.circle(75)

# 14.
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.goto(100, 0)
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)
turtle.end_fill()
turtle.clear()

# 15.
turtle.goto(100, 0)
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)
turtle.penup()
turtle.goto(50, 10)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.done()