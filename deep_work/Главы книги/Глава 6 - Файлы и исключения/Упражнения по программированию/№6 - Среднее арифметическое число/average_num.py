# Программа выводит среднее арифметическое чисел а файле numbers.txt

def main():
    # Накопитель для количества
    total_line = 0

    # Накопитель для суммы чисел
    total_numbers = 0

    # Открытие файла(шаг 1)
    numbers_file = open('numbers.txt', 'r')

    # Цикл читающий строки
    for line in numbers_file:
        # Обработка файла (шаг 2)
        file = float(line)

        # Расчет суммы чисел
        total_numbers += file
        
        # Расчет кол-ва чисел
        total_line += 1
    
    # Расчет среднего арифметического
    average = total_numbers / total_line

    # Вывод итога
    print(average)

    # Закрытие файла(шаг 3)
    numbers_file.close()

if __name__ == '__main__':
    main()