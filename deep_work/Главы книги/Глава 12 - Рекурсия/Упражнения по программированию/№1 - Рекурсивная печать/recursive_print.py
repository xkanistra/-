# Функция выводит рекурсивно числа от 1 до n


def main():
    start = 1
    number = int(input("Введите число: "))
    rec_print(start, number)


# В функцию передали два аргумента, потому что иначе
# невозможно контролировать точку старта и конца рекурсии
# либо вывод будет от n к 1
def rec_print(start, end):
    if start < end + 1:
        print(start)
        rec_print(start + 1, end)


if __name__ == "__main__":
    main()
