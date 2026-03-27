# Программа читает файл со случайными числами и выводит их сумму и кол-во

def main():
    # Накопитель для количества
    total_line = 0

    # Накопитель для суммы чисел
    total_numbers = 0
    
    # Открытие файла(шаг 1)
    file = open('random_num.txt', 'r')

    # Цикл записывающий нужное кол-во строк
    for line in file:
        # Обработка файла (шаг 2)
        amount = float(line)

        # Расчет суммы чисел
        total_numbers += amount

        # Расчет кол-ва чисел
        total_line += 1

    # Вывод итога
    print(f'Всего чисел: {total_line}\nИх сумма: {total_numbers}')
    
    # Закрытие файла(шаг 3)
    file.close()

if __name__ == '__main__':
    main()