# Программа применяет рекурсию
# для нахождения факториала числа


def main():
    # Получить от пользователя число
    number = int(input("Введите неотрицательное число: "))

    # Получить факториал числа
    fact = factorial(number)

    # Показать факториал
    print(f"Факториал числа {number} равняется {fact}")


# Функция применяет рекурсию для вычисления факториала числа
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == "__main__":
    main()
