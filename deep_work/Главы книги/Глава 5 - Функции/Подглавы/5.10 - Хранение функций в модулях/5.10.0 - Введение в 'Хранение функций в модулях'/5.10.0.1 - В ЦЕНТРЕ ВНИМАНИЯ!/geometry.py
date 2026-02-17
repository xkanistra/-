# Программа позволяет выбирать различные
# геометрические вычисления из меню.
# Программа импортирует модули circle и rectangle
import circle
import rectangle

# Константы для элементов меню
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGE_CHOICE = 4
QUIT_CHOICE = 5

# Главная функция
def main():
    # Переменная choice управляет циклом
    # и содержит варианты выборы пользователя
    choice = 0

    while choice != QUIT_CHOICE:
        # Показать меню
        display_menu()

        # Получить варианты выбора пользователя
        choice = int(input('Выберите вариант: '))

        # Выполнить выбранное действие
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print('Площадь равна', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print('Длинна окружности равна',
                circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            lendth = float(input('Введите длину прямоугольника: '))
            print('Площадь равна', rectangle.area(width, lendth))
        elif choice == PERIMETER_RECTANGE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            lendth = float(input('Введите длину прямоугольника: '))
            print('Периметр равен', 
                rectangle.area(width, lendth))
        elif choice == QUIT_CHOICE:
            print('Выходим из программы...')
        else:
            print('Ошибка: недопустимый выбор.')

# Функция display_menu показывает меню
def display_menu():
    print(' МЕНЮ')
    print('1. Площадь круга')
    print('2. Длинна окружности')
    print('3. Площадь прямоугольника')
    print('4. Периметр прямоугольника')
    print('5. Выход')

main()