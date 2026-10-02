# Программа рекурсивно выводит умножение как сумму числа


def main():
    num1 = int(input("Введите число 1: "))
    num2 = int(input("Введите число 2: "))
    rec_multiplic(num1, num2)


def rec_multiplic(x, y):
    if 0 < x:
        print(y)
        rec_multiplic(x - 1, y)

main()
