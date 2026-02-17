# Программа демонстрирует функцию sqrt.
import math

def main():
    # Получить число
    number = float(input('Введите число: '))

    # Получить квадратный корень числа
    square_root = math.sqrt(number)

    # Показать квадратный корень числа
    print(f'Квадратный корень из {number} состовляет {square_root}.')

main()