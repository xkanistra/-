# Сумма чисел

num = int(input('Введите положительное число: '))
total = 0.0

while num > 0:
    total += num
    num = int(input('Введите следующее, либо 0 для остановки: '))

print(total)