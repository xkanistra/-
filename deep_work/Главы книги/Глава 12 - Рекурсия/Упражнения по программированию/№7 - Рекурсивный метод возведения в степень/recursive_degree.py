# Программа рекурсивно возводит числа в степень


def main():
    number = int(input("Введите число которое хотите возвести в степень: "))
    degree = int(input("Введите степень в которую хотите возвести число: "))
    print(rec_degree(number, degree))


def rec_degree(num, degr):
    if degr == 1:
        return num
    elif degr == 0:
        return 1
    elif num == 0:
        return 0
    else:
        return num * rec_degree(num, degr - 1)


if __name__ == "__main__":
    main()
