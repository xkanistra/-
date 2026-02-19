# Написать функцию которая возвращает значение аргумента вдвое меньше

def main():
    number = float(input('Введите число: '))
    result = half(number)
    print(result)

def half(num):
    return num / 2

main()