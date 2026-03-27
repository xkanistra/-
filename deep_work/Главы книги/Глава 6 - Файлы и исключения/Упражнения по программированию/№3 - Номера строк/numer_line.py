# Программа выводит содержимое файла с нумеровкой строк

def main():
    # Запрос название файла
    filename = input('Введите имя файла: ')

    # Открытие файла(шаг 1)
    file = open(filename, 'r')

    # Накопитель
    total = 0
    
    # Цикл считающий строки
    for line in file:
        # Обработка файла (шаг 2)
        amount = line
        amount = amount.rstrip('\n')
        total += 1
        print(f'{total}. {amount}')
    
    # Закрытие файла(шаг 3)
    file.close()
    
if __name__ == '__main__':
    main()