# Программа выводит среднее арифметическое чисел а файле numbers.txt

def main():
    # Группа try
    try:
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

        # Закрытие файла(шаг 3)
        numbers_file.close()

    # Выражния except
    except IOError:
        print('Ошибка при работе с файлом')
    except ValueError:
        print(f'Ошибка при выполнении конвертации значений из файла в строке {total_line + 1}')

    finally:
        # Расчет среднего арифметического
        average = total_numbers / total_line

        # Вывод итога
        print(f'Среднее арифметическое считанных чисел: {average}\nВсего прочитанно чисел: {total_line}')

if __name__ == '__main__':
    main()