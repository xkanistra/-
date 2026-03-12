def main():
    data_file = open('Главы книги/Глава 6 - Файлы и исключения/Подглавы/6.2 - Применение циклов для обработки файлов/data.txt', 'r')
    line = data_file.readline()

    while line!= '':
        amount = int(line)  
        print(f'{amount}')

        line = data_file.readline()

    data_file.close()

if __name__ == '__main__':
    main()
