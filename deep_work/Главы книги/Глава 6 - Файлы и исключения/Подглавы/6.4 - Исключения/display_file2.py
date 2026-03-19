# Программа показывет содержимое файла и корректно откликается на исключение

def main():
    try:
        # Имя файла
        filename = input('Введите имя файла: ')

        # Открыть файл
        infile = open(filename, 'r')

        # Прочитать содержимое
        contents = infile.read()

        # Показать содержимое
        print(contents)

        infile.close()
    
    except IOError:
        print('Произошла ошибка при попытке прочитать\n'
              'файл', filename)

if __name__ == '__main__':
    main()