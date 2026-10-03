# Программа демонстрирует рекурсивную функцию Аккермана


def main():
    m = int(input("Введите число m: "))
    n = int(input("Введите число n: "))
    print(accerman_func(m, n))


def accerman_func(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return accerman_func(m - 1, 1)
    else:
        return accerman_func(m - 1, accerman_func(m, n - 1))


if __name__ == "__main__":
    main()
