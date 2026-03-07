# Программа пишет три строки данных
# в файл
def main():
    # Открыть файл с именем philosophers.txt
    outline = open(r'deep_work/Главы книги/Глава 6 - Файлы и исключения/Подглавы/6.1 - Введение в файловый ввод и вывод/philosophers.txt', 'w')

    # Записать имена трех философов
    # в файл
    outline.write('Джон Локк\n')
    outline.write('Дэвид Хьюм\n') 
    outline.write('Эдмунд Берк\n')

    # Закрытие файла
    outline.close()

# Вызвать глав функцию
if __name__ == '__main__':
    main()