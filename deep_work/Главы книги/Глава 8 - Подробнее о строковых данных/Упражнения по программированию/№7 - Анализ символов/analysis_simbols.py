# Программа анализирует кол-во символов по нескольким критериям из текста в файле
DATA_FILE = "Главы книги/Глава 8 - Подробнее о строковых данных/Упражнения по программированию/Условия для задач/text.txt"

def main():
    str_file = open_file()
    anlys = analysis_string(str_file)

def open_file():
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        lines = file.read()
    return lines


def analysis_string(str_file):
    total_lower = 0
    total_upper = 0
    total_digit = 0
    total_space = 0 
    for ch in str_file:
        if ch.isupper():
            total_upper += 1
        elif ch.islower():
            total_lower += 1
        elif ch.isdigit():
            total_digit += 1
        elif ch.isspace():
            total_space += 1

    print(f'Букв в верхнем регистре: {total_upper}\n'
          f'Букв в нижнем регистре: {total_lower}\n'
          f'Количество цифр: {total_digit}\n'
          f'Количество пробелов: {total_space}')
    

if __name__ == '__main__':
    main()