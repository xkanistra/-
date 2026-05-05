# Программа вычисляет факториал числа
number = int(input(f"Введите число для расчета факториала: "))


def main():
    NotRecFactorial = not_rec_facrtorial(number)
    print("Стандартный метод", NotRecFactorial, sep=" = ")
    print()
    RecFactorial = rec_factorial(number)
    print("Рекурсивный метод", RecFactorial, sep=" = ")
    print()


# Стандартный метод
def not_rec_facrtorial(number):
    the_product = 1
    while number > 0:
        the_product *= number
        number = number - 1
    return the_product


# Метод рекурсии
def rec_factorial(number):
    # Терминальная ветвь, когда функция начинается if возвращает False
    if number == 0:
        return 1
    return number * rec_factorial(number - 1)


if __name__ == "__main__":
    main()
