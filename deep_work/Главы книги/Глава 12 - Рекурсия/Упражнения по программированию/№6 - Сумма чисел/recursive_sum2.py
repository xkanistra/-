# Программа рекурсивно расчитывает сумму чисел от 1 до n


def main():
    start = 1
    end = int(input("Введите число: "))
    print(rec_sum(start, end))


def rec_sum(start, end):
    if start > end:
        return 0
    if start == end:
        return start
    return start + end + rec_sum(start + 1, end - 1)
    


main()
