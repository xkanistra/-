# Программа применяет рекурсию для печати чисел
# последовательности Фибаначчи


def main():
    print("Первые 10 чисел")
    print("последовательности Фибаначчи:")

    for number in range(1, 11):
        print(fib(number))


# Функция возврщает n-ое число
# последовательности Фибоначчи
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    main()
