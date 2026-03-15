# Программа показывает записи, которые
# находятся в файле employees.txt

def main():
    # Открыть файл
    emp_file = open('Главы книги/Глава 6 - Файлы и исключения/Подглавы/6.3 - Обработка записей/employee.txt', 'r')
    # Прочитать первую строку в файле
    name = emp_file.readline()

    # Если поле прочитанно то продолжить обработку
    while name != '':
        # Прочитать номер в инд.номером
        id_num = emp_file.readline()

        # Прочитать поле с названием отдела
        dept = emp_file.readline()

        # Удалить символы новой строки из полей
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Показать записи
        print(f'Имя: {name}')
        print(f'ID: {id_num}')
        print(f'Отдел: {dept}')
        print()

        # Прочитать следующее поле
        name = emp_file.readline()

    # Закрыть файл
    emp_file.close()    

if __name__ == '__main__':
    main()