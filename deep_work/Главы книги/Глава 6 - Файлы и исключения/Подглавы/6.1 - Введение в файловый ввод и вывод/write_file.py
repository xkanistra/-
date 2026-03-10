# Программа дозаписывает данные в существующий файл
# friends.txt
def main():
    # Открыть файл с именем friends.txt
    myfile = open('Главы книги/Глава 6 - Файлы и исключения/Подглавы/6.1 - Введение в файловый ввод и вывод/friends.txt', 'a')

    # Запимать имена в файл
    myfile.write('Лиза\n')
    myfile.write('Кирилл\n')
    myfile.write('Глеб\n')

    # Закрыть файл
    myfile.close()
    
if __name__ == '__main__':
    main()