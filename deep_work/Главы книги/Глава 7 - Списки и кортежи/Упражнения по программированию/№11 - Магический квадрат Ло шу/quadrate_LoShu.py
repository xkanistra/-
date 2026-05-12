# Имитация квадрата Ло Шу
import random

ROWS = 3
COLS = 3


def main():
    LoShu, result = value_list()
    print(LoShu, '\n', result)


def value_list():
    value = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for r in range(ROWS):
        for c in range(COLS):
            print(f'Введите число')
            value[r][c] = int(input())
    if value[0][0] + value[0][1] + value[0][2] == value[1][0] + value[1][1] + value[1][2] == value[1][0] \
                + value[1][1] + value[1][2] == value[2][0] + value[2][1] + value[2][2] == value[0][2] \
                + value[1][2] + value[2][2] == value[0][0] + value[1][1] + value[2][2]:
        result = 'Квадрат Ло Шу'
    else:
        result = 'Не квадрат Ло Шу'
    return value, result


if __name__ == "__main__":
    main()
