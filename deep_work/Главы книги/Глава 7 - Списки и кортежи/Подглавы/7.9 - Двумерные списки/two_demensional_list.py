# Демонстрация работы с двумерными списками при помощи цикла for


def main():
    # Список
    value = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

    # Вывод элементов списка
    for row in value:
        for element in row:
            print(element)


if __name__ == "__main__":
    main()
