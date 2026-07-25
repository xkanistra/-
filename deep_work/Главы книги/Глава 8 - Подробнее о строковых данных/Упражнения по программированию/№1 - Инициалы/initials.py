# Программа показывает инициалы ФИО

def main():
    first_name, last_name, patronymic = get_name()
    full_name = get_full_name(first_name, last_name, patronymic)

def get_name():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    patronymic = input('Введите свое отчество: ')
    return first_name, last_name, patronymic

def get_full_name(first_name, last_name, patronymic):
    print(first_name.upper()[0], last_name.upper()[0], patronymic.upper()[0], sep = '.')
if __name__ == '__main__':
    main()