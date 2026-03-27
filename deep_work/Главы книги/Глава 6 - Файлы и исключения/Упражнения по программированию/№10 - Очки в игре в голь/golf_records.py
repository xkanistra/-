# Программа записывает в файл данные о игроках
# Имя, очки

def main():
    # Флаг работы цикла
    found = 'д'

    # Накопитель для нумерации 
    total = 0
    
    # Открытие файла(шаг 1)
    golf_file = open('golf.txt', 'w')
    
    # Цикл для записи данных в файл
    while found == 'д' or found == 'Д':
        total += 1
        # Внесение данных о имени и очках
        name = input(f'Введите имя игрока {total}: ')
        score = int(input(f'Введите счет игрока {total}: '))

        # Обработка файла (шаг 2)
        golf_file.write(f'Игрок №{total}\n')
        golf_file.write(f'{name}\n')
        golf_file.write(f'{score}\n')

        # Управление циклом
        found = input('Введите д, если желаете добавить игрока (другое значение остановит запись): ')

    # Закрытие файла(шаг 3)
    golf_file.close()

    print('Данные записаны в файл')

if __name__ == '__main__':
    main()