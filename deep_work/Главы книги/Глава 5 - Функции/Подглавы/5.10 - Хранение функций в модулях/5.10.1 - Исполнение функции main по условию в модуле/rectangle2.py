# Функция area принимает ширину и
# длинну прямоугольника в качестве аргументов и возвращает площать прямоугольника 
def area(width, lendth):
    return width * lendth

# Функция perimeter принимает ширину и
# длинну прямоугольника в качестве аргументов и возвращает периметр прямоугольника 
def perimeter(width, lendth):
    return (width + lendth) * 2

# Функция main используется для тестирования другой функции
def main():
    width = float(input('Введите ширину прямоугольника: '))
    lendth = float(input('Введите длину прямоугольника: '))
    print('Площадь равна:', area(width, lendth) )
    print('Периметр равен:', perimeter(width, lendth))

# Вызываем функцию main, ТОЛЬКО ЕСЛИ ФАЙЛ ЗАПУСКАЕТСЯ КАК
# ОТДЕЛЬНАЯ ПРОГРАММА
if __name__ == '__main__':
    main()