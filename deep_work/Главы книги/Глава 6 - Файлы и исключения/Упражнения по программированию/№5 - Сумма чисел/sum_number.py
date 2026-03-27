# Программа выводит сумму чисел а файле numbers.txt

def main():
    # Накопитель
    total = 0

    # Открытие файла(шаг 1)
    numbers_file = open('numbers.txt', 'r')

    # Цикл читающий строки
    for line in numbers_file:
        # Обработка файла (шаг 2)
        file = float(line)
        total += file
    
    # Вывод суммы
    print(total)

    # Закрытие файла(шаг 3)
    numbers_file.close()

if __name__ == '__main__':
    main()

          