# Вычисление факториала.

print('~'*2,'Программа для вычисления факторила','~'*2)

num = int(input('Введите неотрицательное число: '))
total = 1

for n in range(1, num + 1):
    total *= n

print(total)