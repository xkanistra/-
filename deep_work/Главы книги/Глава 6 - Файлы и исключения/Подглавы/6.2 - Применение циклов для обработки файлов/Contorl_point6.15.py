def main():
    data_file = open('Главы книги/Глава 6 - Файлы и исключения/Подглавы/6.2 - Применение циклов для обработки файлов/data.txt', 'r')

    for line in data_file:
        amount = int(line)  
        print(f'{amount}')

    data_file.close()

if __name__ == '__main__':
    main()
