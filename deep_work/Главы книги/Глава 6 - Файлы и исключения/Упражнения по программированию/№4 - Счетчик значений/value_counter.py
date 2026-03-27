# Программа выводит кол-во имен в файле names.txt

def main():
    # Накопитель
    total = 0

    # Открытие файла(шаг 1)
    names_file = open('names.txt', 'r')

    # Цикл считающий строки
    for line in names_file:
        # Обработка файла (шаг 2)
        amount = line
        # Подсчет кол-ва строк
        total += 1
    print(f'Кол-во имен: {total}')
    
    # Закрытие файла(шаг 3)
    names_file.close()
    
if __name__ == '__main__':
    main()