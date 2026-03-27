# Программа выврдит данные о игроках
# Имя, очки

def main():
    # Открытие файла(шаг 1)
    golf_file = open('golf.txt', 'r')

    # Обработка файла (шаг 2)
    # Читаем первую строку
    line = golf_file.readline()

    # Цикл для чтения строк в файле
    while line != '':
        # Чтение строки с именем
        name = golf_file.readline()

        # Чтение строки с очками
        score = float(golf_file.readline())
        
        # Удаление \n
        line = line.rstrip('\n')
        name = name.rstrip('\n')
        
        # Показать записи
        print(line)
        print(name)
        print(score)
        
        # Прочитать след строку
        line = golf_file.readline()

    # Закрыть файл(шаг 3)
    golf_file.close()

if __name__ == '__main__':
    main()